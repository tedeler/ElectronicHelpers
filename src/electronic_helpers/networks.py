"""Resistor/capacitor networks and voltage dividers."""

from __future__ import annotations

from ._validate import positive


def series(*values: float) -> float:
    """Series resistance (or parallel capacitance sum)."""
    if not values:
        raise ValueError("At least one value required")
    return float(sum(values))


def parallel(*values: float) -> float:
    """Parallel resistance. A value of 0 short-circuits to 0."""
    if not values:
        raise ValueError("At least one value required")
    if any(v < 0 for v in values):
        raise ValueError("Values must be >= 0")
    if any(v == 0 for v in values):
        return 0.0
    return 1.0 / sum(1.0 / v for v in values)


def parallel_capacitance(*values: float) -> float:
    """Capacitors in parallel add."""
    return series(*values)


def series_capacitance(*values: float) -> float:
    """Capacitors in series combine like parallel resistors."""
    return parallel(*values)


def voltage_divider(u_in: float, r1: float, r2: float) -> float:
    """Output across r2: Uin * R2 / (R1 + R2)."""
    positive(r1=r1, r2=r2)
    return u_in * r2 / (r1 + r2)


def voltage_divider_resistor(u_in: float, u_out: float, r1: float) -> float:
    """Find R2 for a desired output voltage given R1."""
    positive(r1=r1)
    if not 0 < u_out < u_in:
        raise ValueError("Require 0 < u_out < u_in")
    return r1 * u_out / (u_in - u_out)


