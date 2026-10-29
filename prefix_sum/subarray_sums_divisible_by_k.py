from typing import List

import pytest


# https://leetcode.com/problems/subarray-sums-divisible-by-k/
class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        res = 0
        prefix_sum = 0
        reminder_count = {0: 1}  # edge case: to include subarray if the whole nums are valid

        for n in nums:
            prefix_sum += n
            reminder = prefix_sum % k

            if reminder in reminder_count:
                res += reminder_count[reminder]

            reminder_count[reminder] = 1 + reminder_count.get(reminder, 0)

        return res



sol = Solution()
# time complexity O(n)
# memory complexity O(k) depends on dividers of k



@pytest.mark.parametrize(
    "nums, k, expected", [
    ([4,5,0,-2,-3,1], 5, 7),
    ([5], 9, 0)
    ]
)
def test_subarraysDivByK(nums, k, expected):
    assert sol.subarraysDivByK(nums, k) == expected
