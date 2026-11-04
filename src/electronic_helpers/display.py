"""Pretty printing of electrical quantities."""

from __future__ import annotations

import inspect
from typing import Any

from .units import format_si

try:  # optional
    from IPython.display import HTML, display

    IN_JUPYTER = True
except ImportError:  # pragma: no cover
    IN_JUPYTER = False

UNIT_MAP = {"R": "Ω", "U": "V", "I": "A", "P": "W", "C": "F", "L": "H", "B": ""}
_CHUNK = 3


def _arg_names(count: int) -> list[str]:
    frame = inspect.currentframe()
    try:
        caller = frame.f_back.f_back if frame and frame.f_back else None
        ctx = inspect.getframeinfo(caller).code_context if caller else None
        text = "".join(ctx).strip() if ctx else ""
        raw = text.split("(", 1)[1].rsplit(")", 1)[0]
        names = [n.strip() for n in raw.split(",") if n.strip()]
        if len(names) == count:
            return names
    except Exception:
        pass
    return [f"var_{i}" for i in range(count)]


def _rows(names: list[str], values: tuple[Any, ...]) -> list[list[str]]:
    cells = []
    for name, value in zip(names, values):
        unit = UNIT_MAP.get(name[:1].upper(), "")
        text = format_si(float(value), unit)
        number, _, u = text.partition(" ")
        cells.append([name, number, u])
    rows = []
    for i in range(0, len(cells), _CHUNK):
        row = [c for cell in cells[i:i + _CHUNK] for c in cell]
        row += [""] * (_CHUNK * 3 - len(row))
        rows.append(row)
    return rows


def print_el(*values: float, names: list[str] | None = None) -> None:
    """Print variables in blocks of three (name, value, unit).

    Names are taken from the call expression unless ``names`` is given. The first
    letter of the name selects the unit (R, U, I, P, C, L).
    """
    names = names or _arg_names(len(values))
    rows = _rows(names, values)
    header = ["Variable", "Wert", "Einheit"] * _CHUNK
    if IN_JUPYTER and _in_notebook():

        def cells(tag: str, r: list[str]) -> str:
            return "".join(
                f"<{tag} style='padding:6px 14px;text-align:left"
                f"{';border-right:2px solid #a0a0a0' if k % 3 == 2 else ''}'>{c}</{tag}>"
                for k, c in enumerate(r)
            )

        html = "<table><tr>" + cells("th", header) + "</tr>"
        html += "".join("<tr>" + cells("td", r) + "</tr>" for r in rows) + "</table>"
        display(HTML(html))
        return
    table = [header, *rows]
    widths = [max(len(r[k]) for r in table) for k in range(len(header))]
    for r in table:
        print("  ".join(c.ljust(w) for c, w in zip(r, widths)).rstrip())


def _in_notebook() -> bool:
    try:
        from IPython import get_ipython

        shell = get_ipython()
        return shell is not None and shell.__class__.__name__ == "ZMQInteractiveShell"
    except Exception:  # pragma: no cover
        return False


def printEL(*values: float) -> None:
    """Backwards-compatible alias for :func:`print_el`."""
    print_el(*values, names=_arg_names(len(values)))
