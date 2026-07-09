import pytest

from calc.calc import moving_average, percent, running_total


def test_percent_basic():
    assert percent(1, 4) == 25.0


def test_running_total():
    assert running_total([1, 2, 3]) == [1.0, 3.0, 6.0]


def test_moving_average_basic():
    assert moving_average([1, 2, 3, 4], 2) == [1.5, 2.5, 3.5]


def test_moving_average_window_one():
    assert moving_average([1, 2, 3], 1) == [1.0, 2.0, 3.0]


def test_moving_average_window_larger_than_input():
    assert moving_average([1, 2], 3) == []


def test_moving_average_invalid_window():
    with pytest.raises(ValueError):
        moving_average([1, 2, 3], 0)
