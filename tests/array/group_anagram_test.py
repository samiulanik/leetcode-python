from operator import itemgetter

from solutions.array import group_anagram


def test_case_1():
    expected = []
    for e in [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]:
        expected.append(sorted(e))

    actual = []
    for a in group_anagram.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]):
        actual.append(sorted(a))

    assert sorted(expected) == sorted(actual)
