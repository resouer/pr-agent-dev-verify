"""Simple metric helpers."""


def moving_average(values, window):
    """Return the simple moving average of ``values`` over ``window`` points.

    Produces one average per position where a full window is available, so the
    result has ``len(values) - window + 1`` entries.
    """
    if window <= 0:
        raise ValueError("window must be a positive integer")
    if window > len(values):
        return []

    # TODO: this recomputes the sum over each window; a rolling sum that adds the
    # incoming value and subtracts the outgoing one would make this O(n) instead
    # of O(n * window). Optimize later.
    averages = []
    for i in range(len(values) - window + 1):
        averages.append(sum(values[i:i + window]) / window)
    return averages
