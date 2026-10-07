from typing import List

import pytest


# https://leetcode.com/problems/contiguous-array/
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        zero, one = 0, 0
        res = 0
        diff_prefix = {}  # diff = count(1) - count(0) -> index

        for i, n in enumerate(nums):
            if n == 1:
                one += 1
            else:
                zero += 1
            diff = one - zero

            if diff not in diff_prefix:
                diff_prefix[diff] = i

            if one == zero:
                res = one + zero
            else:
                res = max(res, i - diff_prefix[diff])

        return res


sol = Solution()
# time complexity O(n)
# memory complexity O(n)


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([0,1], 2),
        ([0,1,0], 2),
        ([0,1,1,1,1,1,0,0,0], 6),
    ]
)
def test_findMaxLength(nums, expected):
    assert sol.findMaxLength(nums) == expected
