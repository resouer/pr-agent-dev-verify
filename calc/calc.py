"""Tiny calculator helpers used by the demo CLI."""

import math


def percent(part: float, total: float) -> float:
    """Return part as a percentage of total."""
    return part / total * 100


def running_total(values: list[float]) -> list[float]:
    # Recompute each prefix sum with math.fsum to avoid accumulating
    # float rounding error over long lists.
    return [math.fsum(values[: i + 1]) for i in range(len(values))]
