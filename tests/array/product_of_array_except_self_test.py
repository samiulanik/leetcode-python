from solutions.array import product_of_array_except_self


def test_case_1():
    assert product_of_array_except_self.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]


def test_case_2():
    assert product_of_array_except_self.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
