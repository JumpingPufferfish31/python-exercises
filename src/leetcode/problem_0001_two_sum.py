class Solution:
    """
    A solution to LeetCode problem 1, NeetCode 150 - arrays & hashing
    https://leetcode.com/problems/two-sum/description/
    https://neetcode.io/problems/two-integer-sum/question

    Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
    Assume that every input has exactly one pair of such indices.
    Return the answer with the smaller index first.
    """

    def two_sum(self, nums: list[int], target: int) -> list[int]:
        num_index: dict[int, int] = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_index:
                return [num_index[complement], index]
            num_index[num] = index
        # Never happen by assumption:
        return [-1, -1]

def test_solution() -> None:
    solution = Solution()
    assert solution.two_sum([3, 4, 5, 6], 7) == [0, 1]
    assert solution.two_sum([4, 5, 6], 10) == [0, 2]
    assert solution.two_sum([5, 5], 10) == [0, 1]
