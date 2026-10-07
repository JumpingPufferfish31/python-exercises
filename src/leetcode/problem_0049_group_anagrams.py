from utils.list import sort_nested


class Solution:
    """
    A solution to LeetCode problem 49, NeetCode 150 - arrays & hashing
    https://leetcode.com/problems/group-anagrams/description/
    https://neetcode.io/problems/anagram-groups/question

    Given an array of strings, group all anagrams together into sublists.
    The output can be in any order.
    An anagram is a string that contains the exact same characters as another string regardless of order.
    """

    def group_anagrams(self, strs: list[str]) -> list[list[str]]:
        groups: dict[tuple[int, ...], list[str]] = {}
        index_offset = ord('a')
        for s in strs:
            char_freq = [0] * 26
            for char in s:
                index = ord(char) - index_offset
                char_freq[index] += 1
            key: tuple[int, ...] = tuple(char_freq)
            if key in groups:
                groups[key].append(s)
            else:
                groups[key] = [s]
        return list(groups.values())

def test_solution() -> None:
    solution = Solution()
    assert sort_nested(solution.group_anagrams([])) == sort_nested([])
    assert sort_nested(solution.group_anagrams(["x"])) == sort_nested([["x"]])
    assert sort_nested(solution.group_anagrams(["act", "pots", "tops", "cat", "stop", "hat"])) == sort_nested(
        [["hat"], ["act", "cat"], ["stop", "pots", "tops"]])