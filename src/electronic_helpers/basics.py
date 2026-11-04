"""Ohm's law, power, reactance and LED helpers (SI base units)."""

from __future__ import annotations

import math

from ._validate import positive


def voltage(i: float, r: float) -> float:
    """U = I * R."""
    return i * r


def current(u: float, r: float) -> float:
    """I = U / R."""
    positive(r=r)
    return u / r


def resistance(u: float, i: float) -> float:
    """R = U / I."""
    if i == 0:
        raise ValueError("i must not be 0")
    return u / i


def power(u: float | None = None, i: float | None = None, r: float | None = None) -> float:
    """Power from exactly two of voltage, current, resistance."""
    given = [x is not None for x in (u, i, r)]
    if sum(given) != 2:
        raise ValueError("Provide exactly two of u, i, r")
    if u is not None and i is not None:
        return u * i
    if i is not None and r is not None:
        return i * i * r
    assert u is not None and r is not None
    positive(r=r)
    return u * u / r


def angular_frequency(f: float) -> float:
    """ω = 2πf."""
    return 2 * math.pi * f


def capacitive_reactance(c: float, f: float) -> float:
    """X_C = 1 / (2πfC) in Ω."""
    positive(c=c, f=f)
    return 1 / (angular_frequency(f) * c)


def inductive_reactance(l: float, f: float) -> float:  # noqa: E741
    """X_L = 2πfL in Ω."""
    positive(l=l, f=f)
    return angular_frequency(f) * l


def led_series_resistor(u_supply: float, u_led: float, i_led: float) -> float:
    """Series resistor for an LED: (Us - Uf) / If."""
    positive(i_led=i_led)
    if u_supply <= u_led:
        raise ValueError("u_supply must exceed u_led")
    return (u_supply - u_led) / i_led
