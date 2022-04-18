# https://leetcode.com/problems/container-with-most-water/

def maxArea(height: list[int]) -> int:
    left, right = 0, len(height) - 1
    res = min(height[left], height[right]) * (right - left)

    while left < right:
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
        res = max(res, min(height[left], height[right]) * (right - left))
    return res
