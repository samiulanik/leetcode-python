from solutions.backtracking import subsets_with_dup


def test_case_1():
    expected = [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
    actual = subsets_with_dup.subsetsWithDup([1, 2, 2])
    assert sorted(expected) == sorted(actual)
