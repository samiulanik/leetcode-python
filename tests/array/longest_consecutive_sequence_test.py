from solutions.array import longest_consecutive_sequence


def test_case_1():
    assert longest_consecutive_sequence.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4


def test_case_2():
    assert longest_consecutive_sequence.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
