from solutions.binary_search import search_a_2d_matrix


def test_case_1():
    assert search_a_2d_matrix.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3) is True


def test_case_2():
    assert search_a_2d_matrix.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13) is False


def test_case_3():
    assert search_a_2d_matrix.searchMatrix([[1]], 1) is True
