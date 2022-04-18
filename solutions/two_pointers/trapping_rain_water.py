# https://leetcode.com/problems/trapping-rain-water/


def trap(height: list[int]) -> int:
    res = 0
    if not height:
        return res
    size = len(height)
    left, right = 0, size - 1
    left_max, right_max = height[left], height[right]

    while left < right:
        if left_max < right_max:
            left += 1
            left_max = max(left_max, height[left])
            res += left_max - height[left]
        else:
            right -= 1
            right_max = max(right_max, height[right])
            res += right_max - height[right]
    return res
