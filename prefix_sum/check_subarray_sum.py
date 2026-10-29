from typing import List

import pytest


# https://leetcode.com/problems/continuous-subarray-sum/
class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        reminder = { 0: -1 }  # map reminder -> end index
        # 0: -1 it's edge case to prevent return True if the 0 index are multiple of k
        total = 0

        for i, n in enumerate(nums):
            total += n
            r = total % k

            if r not in reminder:
                reminder[r] = i
            elif (i - reminder[r]) >= 2:
                return True

        return False


sol = Solution()
# time complexity O(n)
# memory complexity O(n)


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([23,2,4,6,7], 6, True),
        ([23,2,6,4,7], 6, True),
        ([23,2,6,4,7], 13, False),
    ]
)
def test_checkSubarraySum(nums, k, expected):
    assert sol.checkSubarraySum(nums, k) == expected
