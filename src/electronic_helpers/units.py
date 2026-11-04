"""SI prefix formatting and parsing."""

from __future__ import annotations

import math
import re

PREFIXES = {
    12: "T", 9: "G", 6: "M", 3: "k", 0: "",
    -3: "m", -6: "µ", -9: "n", -12: "p", -15: "f",
}
_FROM_PREFIX = {"T": 12, "G": 9, "M": 6, "k": 3, "m": -3, "u": -6, "µ": -6, "n": -9, "p": -12, "f": -15}
_PATTERN = re.compile(r"^\s*([+-]?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)\s*([TGMkmuµnpf]?)\s*[^\W\d_]*\s*$")


def format_si(value: float, unit: str = "", digits: int = 3) -> str:
    """Format ``value`` with an SI prefix, e.g. ``format_si(4700, "Ω") == "4.700 kΩ"``."""
    if value == 0 or not math.isfinite(value):
        return f"{value:.{digits}f} {unit}".strip() if value == 0 else f"{value} {unit}".strip()
    exponent = int(math.floor(math.log10(abs(value)) / 3) * 3)
    exponent = max(min(PREFIXES), min(max(PREFIXES), exponent))
    scaled = value / 10**exponent
    # rounding may push 999.9996 to 1000.000
    if abs(round(scaled, digits)) >= 1000 and exponent < max(PREFIXES):
        exponent += 3
        scaled = value / 10**exponent
    return f"{scaled:.{digits}f} {PREFIXES[exponent]}{unit}".strip()


def parse_si(text: str) -> float:
    """Parse strings like ``"4.7k"``, ``"100nF"``, ``"2.2 MΩ"`` into floats."""
    match = _PATTERN.match(text)
    if not match:
        raise ValueError(f"Cannot parse SI value: {text!r}")
    number, prefix = match.groups()
    return float(number) * 10.0 ** _FROM_PREFIX.get(prefix, 0)
