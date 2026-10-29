from typing import List

import pytest


# https://leetcode.com/problems/find-pivot-index/
class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total = sum(nums)  # O(n)
        left_sum = 0

        for i, n in enumerate(nums):
            if left_sum == total - left_sum - n:
                return i
            left_sum += n

        return -1


sol = Solution()
# time complexity O(n) + O(n) = O(n)
# memory complexity O(1)


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1,7,3,6,5,6], 3),
        ([1,2,3], -1),
        ([2,1,-1], 0),
    ]
)
def test_pivotIndex(nums, expected):
    assert sol.pivotIndex(nums) == expected
