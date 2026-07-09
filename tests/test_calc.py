from calc.calc import percent, running_total


def test_percent_basic():
    assert percent(1, 4) == 25.0


def test_running_total():
    assert running_total([1, 2, 3]) == [1.0, 3.0, 6.0]
