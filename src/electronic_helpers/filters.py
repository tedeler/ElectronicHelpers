"""First-order filter helpers."""

from __future__ import annotations

import math

from ._validate import positive


def rc_time_constant(r: float, c: float) -> float:
    """τ = R·C in seconds."""
    positive(r=r, c=c)
    return r * c


def rc_cutoff_frequency(r: float, c: float) -> float:
    """f_c = 1 / (2πRC) in Hz."""
    return 1 / (2 * math.pi * rc_time_constant(r, c))


def rl_cutoff_frequency(r: float, l: float) -> float:  # noqa: E741
    """f_c = R / (2πL) in Hz."""
    positive(r=r, l=l)
    return r / (2 * math.pi * l)
