"""electronic_helpers: helper functions for electronics."""

from .basics import (
    angular_frequency,
    capacitive_reactance,
    current,
    inductive_reactance,
    led_series_resistor,
    power,
    resistance,
    voltage,
)
from .display import print_el, printEL
from .e_series import E_SERIES, e_series_values, nearest_e_value
from .filters import rc_cutoff_frequency, rc_time_constant, rl_cutoff_frequency
from .networks import (
    parallel,
    parallel_capacitance,
    series,
    series_capacitance,
    voltage_divider,
    voltage_divider_resistor,
)
from .units import format_si, parse_si

__version__ = "0.1.0"

__all__ = [
    "E_SERIES", "angular_frequency", "capacitive_reactance", "current", "e_series_values",
    "format_si", "inductive_reactance", "led_series_resistor", "nearest_e_value",
    "parallel", "parallel_capacitance", "parse_si", "power", "printEL", "print_el",
    "rc_cutoff_frequency", "rc_time_constant", "resistance", "rl_cutoff_frequency",
    "series", "series_capacitance", "voltage", "voltage_divider", "voltage_divider_resistor",
]
