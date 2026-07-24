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

    # Rolling sum: seed with the first window, then slide by adding the incoming
    # value and subtracting the outgoing one. This keeps the whole pass O(n)
    # rather than recomputing each window's sum (O(n * window)).
    window_sum = sum(values[:window])
    averages = [window_sum / window]
    for i in range(window, len(values)):
        window_sum += values[i] - values[i - window]
        averages.append(window_sum / window)
    return averages
