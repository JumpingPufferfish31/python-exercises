class Solution:
    """
    A solution to LeetCode problem 271, NeetCode 150 - arrays & hashing
    https://leetcode.com/problems/encode-and-decode-strings/description/ (requires subscription)
    https://neetcode.io/problems/string-encode-and-decode/question

    Design an algorithm to encode a list of strings to a string and to decode back to the original list of strings.
    """

    unit_separator = "␟"

    def encode(self, strs: list[str]) -> str:
        prefix = f"{len(strs)}{Solution.unit_separator}"
        return f"{prefix}{Solution.unit_separator.join(strs)}"

    def decode(self, s: str) -> list[str]:
        parts = s.split(Solution.unit_separator)
        length = int(parts[0])
        if length == 0:
            return []
        return parts[1:]

def test_solution() -> None:
    solution = Solution()
    list_1: list[str] = ["we", "say", ":", "yes"]
    assert solution.decode(solution.encode(list_1)) == list_1
    list_2: list[str] = []
    assert solution.decode(solution.encode(list_2)) == list_2
    list_3: list[str] = ["foo"]
    assert solution.decode(solution.encode(list_3)) == list_3
    list_4: list[str] = [""]
    assert solution.decode(solution.encode(list_4)) == list_4
