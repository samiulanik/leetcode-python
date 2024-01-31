# dfs call used for the following problems
# https://leetcode.com/problems/subsets/description/
# https://leetcode.com/problems/subsets-ii/description/

def subsets_dfs(index: int, input_nums: list[int], current: list[int], result: list[list[int]]) -> list[list[int]]:
    if index >= len(input_nums):
        if current not in result:
            result.append(current)
        return
    subsets_dfs(index + 1, input_nums, current + [input_nums[index]], result)
    subsets_dfs(index + 1, input_nums, current, result)
    return result
