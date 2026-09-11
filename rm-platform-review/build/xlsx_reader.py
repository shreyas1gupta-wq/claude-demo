"""Minimal read-only .xlsx reader built on the standard library only.

This environment has no openpyxl/pandas and the build must not add a
dependency, so the workbook is read straight out of its zip container.

A sheet is returned as ``{row_number: {col_number: value}}`` with 1-based
indices and empty cells omitted.  ``formulas=True`` returns
``(value, formula_text)`` tuples instead, which is what lets the build prove
whether a given cell is live or a stale typed constant.
"""

import zipfile
from xml.etree import ElementTree as ET

_MAIN = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
_REL = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"


def col_to_num(ref):
    """'AB12' -> 28.  Stops at the first digit."""
    n = 0
    for ch in ref:
        if not ch.isalpha():
            break
        n = n * 26 + ord(ch.upper()) - 64
    return n


def num_to_col(n):
    """28 -> 'AB'."""
    s = ""
    while n:
        n, r = divmod(n - 1, 26)
        s = chr(65 + r) + s
    return s


def _coerce(text):
    """Numeric strings become int/float; everything else stays a string."""
    try:
        f = float(text)
    except (TypeError, ValueError):
        return text
    return int(f) if f == int(f) else round(f, 6)


class Workbook:
    def __init__(self, path):
        self._zip = zipfile.ZipFile(path)
        self._shared = self._read_shared_strings()
        self.sheets = self._read_sheet_index()

    def _read_shared_strings(self):
        if "xl/sharedStrings.xml" not in self._zip.namelist():
            return []
        root = ET.fromstring(self._zip.read("xl/sharedStrings.xml"))
        # A <si> can be split across several <t> runs; join them in order.
        return [
            "".join(t.text or "" for t in si.iter(_MAIN + "t"))
            for si in root.iter(_MAIN + "si")
        ]

    def _read_sheet_index(self):
        book = ET.fromstring(self._zip.read("xl/workbook.xml"))
        rels = ET.fromstring(self._zip.read("xl/_rels/workbook.xml.rels"))
        targets = {r.get("Id"): r.get("Target") for r in rels}
        index = {}
        for sh in book.iter(_MAIN + "sheet"):
            target = targets[sh.get(_REL + "id")]
            index[sh.get("name")] = {
                "path": "xl/" + target.lstrip("/"),
                "state": sh.get("state") or "visible",
            }
        return index

    def sheet(self, name, formulas=False):
        root = ET.fromstring(self._zip.read(self.sheets[name]["path"]))
        out = {}
        for row in root.iter(_MAIN + "row"):
            cells = {}
            for c in row.iter(_MAIN + "c"):
                kind = c.get("t")
                v = c.find(_MAIN + "v")
                inline = c.find(_MAIN + "is")
                f = c.find(_MAIN + "f")
                if kind == "s" and v is not None:
                    value = self._shared[int(v.text)]
                elif kind == "inlineStr" and inline is not None:
                    value = "".join(t.text or "" for t in inline.iter(_MAIN + "t"))
                elif kind == "str" and v is not None:
                    value = v.text
                elif v is not None:
                    value = _coerce(v.text)
                else:
                    value = None
                col = col_to_num(c.get("r"))
                if formulas:
                    cells[col] = (value, f.text if f is not None else None)
                elif value not in (None, ""):
                    cells[col] = value
            if cells:
                out[int(row.get("r"))] = cells
        return out
