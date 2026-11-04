# electronic-helpers

Python library with helper functions for electronics: Ohm's law, power, reactance,
resistor/capacitor networks, voltage dividers, E-series, RC/RL filters, SI formatting
and a compact `printEL` table output. No runtime dependencies (IPython optional).

## Installation
```bash
upip='uv pip install --python ~/.local/share/python-default-env'
```

```bash
upip electronic-helpers            # or: uv add electronic-helpers
upip "electronic-helpers[notebook]"  # HTML output in Jupyter
upip git+https://github.com/tedeler/ElectronicHelpers
```

## Usage

```python
import electronic_helpers as eh

R1, U_ein, C_1 = 4700, 5, 1e-7
eh.printEL(R1, U_ein, C_1)          # first letter of the name selects the unit
eh.parallel(100, 100)               # 50.0
eh.nearest_e_value(4800, "E12")     # 4700.0
eh.rc_cutoff_frequency(1e3, 1e-6)   # 159.15 Hz
eh.format_si(4700, "Ω")             # '4.700 kΩ'
```

## Development

```bash
uv sync --extra dev
uv run pytest && uv run ruff check . && uv run mypy
uv build
```

Releases: tag `vX.Y.Z` (version lives in `src/electronic_helpers/__init__.py`);
CI publishes to PyPI via trusted publishing.

## License
MIT
