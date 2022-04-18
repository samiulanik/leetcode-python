# https://leetcode.com/problems/3sum/
from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    result, size = [], len(nums)

    if size < 3:
        return result

    nums.sort()
    for i in range(size):
        if i - 1 >= 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, size - 1
        while left < right:
            target = nums[i] + nums[left] + nums[right]
            if target == 0:
                result.append([nums[i], nums[left], nums[right]])
                while left + 1 < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right - 1 and nums[right] == nums[right - 1]:
                    right -= 1
                left, right = left + 1, right - 1
            elif target < 0:
                left += 1
            else:
                right -= 1
    return result
