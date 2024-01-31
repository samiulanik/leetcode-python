# https://leetcode.com/problems/subsets/description/


def subsets(nums: list[int]) -> list[list[int]]:
    return dfs(0, nums, [], [])


def dfs(index: int, input: list[int], current: list[int], result: list[list[int]]) -> list[list[int]]:
    if index >= len(input):
        if current not in result:
            result.append(current)
        return
    dfs(index + 1, input, current + [input[index]], result)
    dfs(index + 1, input, current, result)
    return result
