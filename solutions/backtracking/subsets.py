# https://leetcode.com/problems/subsets/description/
from solutions.backtracking import subsets_dfs


def subsets(nums: list[int]) -> list[list[int]]:
    return subsets_dfs.subsets_dfs(0, nums, [], [])
