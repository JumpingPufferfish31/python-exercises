class Solution:
    """
    A solution to LeetCode problem 242, NeetCode 150 - arrays & hashing
    https://leetcode.com/problems/valid-anagram/description/
    https://neetcode.io/problems/is-anagram/question

    Given two strings, return true if the two strings are anagrams of each other, otherwise return false.
    Two strings are anagrams if they contain the same characters, with each character appearing the same number of times, regardless of order.
    """

    def is_anagram(self, s: str, t: str) -> bool:
        char_freq: dict[str, int] = {}
        for char in s:
            if char in char_freq:
                char_freq[char] += 1
            else:
                char_freq[char] = 1
        for char in t:
            if char not in char_freq:
                return False
            char_freq[char] -= 1
            if char_freq[char] == 0:
                del char_freq[char]
        return len(char_freq) == 0

def test_solution() -> None:
    solution = Solution()
    assert solution.is_anagram("racecar", "carrace")
    assert not solution.is_anagram("jar", "jam")
