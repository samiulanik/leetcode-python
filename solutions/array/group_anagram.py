# https://leetcode.com/problems/group-anagrams/
import collections


def groupAnagrams(strs: list[str]) -> list[list[str]]:
    result = collections.defaultdict(list)

    for s in strs:
        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord("a")] += 1
        result[tuple(count)].append(s)

    return list(result.values())
