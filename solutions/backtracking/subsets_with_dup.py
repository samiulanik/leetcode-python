# https://leetcode.com/problems/subsets-ii/description/
from solutions.backtracking import subsets_dfs


def subsetsWithDup(nums: list[int]) -> list[list[int]]:
    nums = sorted(nums)
    return subsets_dfs.subsets_dfs(0, nums, [], [])
