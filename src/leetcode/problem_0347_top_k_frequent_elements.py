class Solution:
    """
    A solution to LeetCode problem 347, NeetCode 150 - arrays & hashing
    https://leetcode.com/problems/top-k-frequent-elements/description/
    https://neetcode.io/problems/top-k-elements-in-list/question

    Given an integer array nums and an integer k, return the k most frequent elements in nums.
    Assume the answer is always unique.
    The output can be in any order.
    """

    def top_k_frequent(self, nums: list[int], k: int) -> list[int]:
        # O(n) with bucket sort:
        #    - 1 iteration to get the frequencies
        #    - 1 iteration to map each frequency to numbers with that frequency
        #    - 1 iteration to go through frequencies from largest to smallest
        freq = {}
        max_freq = float('-inf')
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
            max_freq = max(max_freq, freq[num])
        if max_freq == float('-inf'):
            return []
        max_freq = int(max_freq)

        nums_with_freq = {}
        for num, count in freq.items():
            if count not in nums_with_freq:
                nums_with_freq[count] = [num]
            else:
                nums_with_freq[count].append(num)

        top_k = []
        nums_included = 0
        for i in range(max_freq, 0, -1):
            if i in nums_with_freq:
                for num in nums_with_freq[i]:
                    top_k.append(num)
                    nums_included += 1
                    if nums_included >= k:
                        return top_k
        return top_k

def test_solution() -> None:
    solution = Solution()
    assert sorted(solution.top_k_frequent([7, 7], 1)) == sorted([7])
    assert sorted(solution.top_k_frequent([1, 2, 2, 3, 3, 3], 2)) == sorted([2, 3])
