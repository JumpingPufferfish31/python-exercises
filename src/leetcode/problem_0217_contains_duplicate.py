class Solution:
    """
    A solution to LeetCode problem 217, NeetCode 150 - arrays & hashing
    https://leetcode.com/problems/contains-duplicate/description/
    https://neetcode.io/problems/duplicate-integer/question

    Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
    """

    def has_duplicate(self, nums: list[int]) -> bool:
        seen: set[int] = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

def test_solution() -> None:
    solution = Solution()
    assert solution.has_duplicate([1, 2, 3, 1])
    assert not solution.has_duplicate([1, 2, 3, 4])
    assert solution.has_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
