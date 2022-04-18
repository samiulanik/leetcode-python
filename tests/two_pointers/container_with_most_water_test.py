from solutions.two_pointers import container_with_most_water


def test_case_1():
    assert container_with_most_water.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49


def test_case_2():
    assert container_with_most_water.maxArea([1, 1]) == 1
