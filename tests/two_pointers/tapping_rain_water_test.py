from solutions.two_pointers import trapping_rain_water


def test_case_1():
    assert trapping_rain_water.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6


def test_case_2():
    assert trapping_rain_water.trap([4, 2, 0, 3, 2, 5]) == 9
