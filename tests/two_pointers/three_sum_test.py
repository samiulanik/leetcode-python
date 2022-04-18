from solutions.two_pointers import three_sum


def test_happy_path():
    assert three_sum.threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]


def test_empty_list():
    assert three_sum.threeSum([]) == []


def test_single_element():
    assert three_sum.threeSum([0]) == []
