import math

import pytest

import electronic_helpers as eh


def test_format_parse():
    assert eh.format_si(4700, "Ω") == "4.700 kΩ"
    assert eh.format_si(0, "V") == "0.000 V"
    assert eh.format_si(0.0000001, "F") == "100.000 nF"
    assert eh.parse_si("4.7k") == pytest.approx(4700)
    assert eh.parse_si("100nF") == pytest.approx(1e-7)
    with pytest.raises(ValueError):
        eh.parse_si("abc")


def test_basics():
    assert eh.voltage(2, 5) == 10
    assert eh.current(10, 5) == 2
    assert eh.power(u=10, r=5) == 20
    with pytest.raises(ValueError):
        eh.power(u=1)
    assert eh.led_series_resistor(5, 2, 0.02) == pytest.approx(150)
    assert eh.capacitive_reactance(1e-6, 1000) == pytest.approx(159.155, rel=1e-4)


def test_networks():
    assert eh.series(1, 2) == 3
    assert eh.parallel(100, 100) == 50
    assert eh.parallel(0, 5) == 0
    assert eh.voltage_divider(10, 1000, 1000) == 5
    assert eh.voltage_divider_resistor(10, 5, 1000) == pytest.approx(1000)


def test_filters():
    assert eh.rc_cutoff_frequency(1000, 1e-6) == pytest.approx(1 / (2 * math.pi * 1e-3))


def test_series():
    assert eh.nearest_e_value(4800) == 4700
    assert eh.nearest_e_value(9900, "E12") == 10000
    assert eh.nearest_e_value(0.5, "E24") == 0.51
    with pytest.raises(ValueError):
        eh.nearest_e_value(1, "E99")


def test_print(capsys):
    R1, U_ein, I_1, C_2 = 4700, 5, 0.002, 1e-7
    eh.printEL(R1, U_ein, I_1, C_2)
    out = capsys.readouterr().out
    assert "R1" in out and "4.700" in out and "kΩ" in out and "nF" in out
