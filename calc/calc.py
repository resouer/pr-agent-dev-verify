"""Tiny calculator helpers used by the demo CLI."""


def percent(part: float, total: float) -> float:
    """Return part as a percentage of total."""
    return part / total * 100


def running_total(values: list[float]) -> list[float]:
    out: list[float] = []
    acc = 0.0
    for v in values:
        acc += v
        out.append(acc)
    return out


def moving_average(values: list[float], window: int) -> list[float]:
    """Return the sliding-window averages of values.

    For each contiguous window of the given size, yields the mean of that
    window. The result has ``len(values) - window + 1`` entries, or is empty
    when the window is larger than the input.
    """
    if window < 1:
        raise ValueError("window must be >= 1")
    out: list[float] = []
    for i in range(len(values) - window + 1):
        out.append(sum(values[i : i + window]) / window)
    return out
