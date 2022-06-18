# https://leetcode.com/problems/longest-consecutive-sequence/

def longestConsecutive(nums: list[int]) -> int:
    num_set = set(nums)
    longest = 0

    for n in nums:
        if (n - 1) not in num_set:
            length = 0
            while (n + length) in num_set:
                length += 1
            longest = max(longest, length)

    return longest
