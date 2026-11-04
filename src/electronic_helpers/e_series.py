"""Preferred number series (IEC 60063)."""

from __future__ import annotations

import math

E_SERIES: dict[str, tuple[float, ...]] = {
    "E3": (1.0, 2.2, 4.7),
    "E6": (1.0, 1.5, 2.2, 3.3, 4.7, 6.8),
    "E12": (1.0, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2),
    "E24": (1.0, 1.1, 1.2, 1.3, 1.5, 1.6, 1.8, 2.0, 2.2, 2.4, 2.7, 3.0,
            3.3, 3.6, 3.9, 4.3, 4.7, 5.1, 5.6, 6.2, 6.8, 7.5, 8.2, 9.1),
}


def e_series_values(series: str, decade_min: int, decade_max: int) -> list[float]:
    """All values of ``series`` from 10**decade_min up to 10**decade_max (inclusive of last decade start)."""
    base = _base(series)
    return [round(b * 10.0**d, 12) for d in range(decade_min, decade_max) for b in base]


def _base(series: str) -> tuple[float, ...]:
    try:
        return E_SERIES[series.upper()]
    except KeyError:
        raise ValueError(f"Unknown series {series!r}; choose from {sorted(E_SERIES)}") from None


def nearest_e_value(value: float, series: str = "E12") -> float:
    """Nearest preferred value (log-distance) from the given E series."""
    if not value > 0:
        raise ValueError("value must be > 0")
    base = _base(series)
    decade = math.floor(math.log10(value))
    candidates = [b * 10.0**d for d in (decade - 1, decade, decade + 1) for b in base + (10.0,)]
    best = min(candidates, key=lambda c: abs(math.log(c / value)))
    return float(f"{best:.6g}")
