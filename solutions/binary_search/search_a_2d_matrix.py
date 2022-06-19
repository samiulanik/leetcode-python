# https://leetcode.com/problems/search-a-2d-matrix/

def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    rows, cols = len(matrix), len(matrix[0])
    top, bottom = 0, rows - 1

    while bottom >= top:
        row = (top + bottom) // 2
        if target > matrix[row][-1]:
            top = row + 1
        elif target < matrix[row][0]:
            bottom = row - 1
        else:
            break

    if not (bottom >= top):
        return False

    row = (top + bottom) // 2
    left, right = 0, cols - 1

    while right >= left:
        middle = (right + left) // 2
        if target > matrix[row][middle]:
            left = middle + 1
        elif target < matrix[row][middle]:
            right = middle - 1
        else:
            return True

    return False
