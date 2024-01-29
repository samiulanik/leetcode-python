from solutions.adhoc import kth_factor_of_n
from solutions.adhoc.kth_factor_of_n import kthFactor


def test_case_1():
    assert kthFactor(12, 3) == 3


def test_case_2():
    assert kthFactor(7, 2) == 7


def test_case_3():
    assert kthFactor(4, 4) == -1
