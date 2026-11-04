from __future__ import annotations


def positive(**values: float) -> None:
    for name, v in values.items():
        if not v > 0:
            raise ValueError(f"{name} must be > 0, got {v!r}")
