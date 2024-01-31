from collections import Counter

from solutions.backtracking import subsets


def test_case_1():
    expected = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    actual = subsets.subsets([1, 2, 3])
    assert sorted(expected) == sorted(actual)


def test_case_2():
    expected = [[], [0]]
    actual = subsets.subsets([0])
    assert sorted(expected) == sorted(actual)
