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
