from typing import List

import pytest


# https://leetcode.com/problems/range-sum-query-immutable/
class NumArray:

    def __init__(self, nums: list[int]):
        self.prefixes = []
        left_sum = 0

        for i in nums:
            left_sum += i
            self.prefixes.append(left_sum)

    def sumRange(self, left: int, right: int) -> int:
        right_sum = self.prefixes[right]
        left_sum = self.prefixes[left - 1] if left > 0 else 0

        return right_sum - left_sum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)


sol = NumArray([-2, 0, 3, -5, 2,-1])
# time complexity O(1)
# memory complexity O(n) if it counts as input


@pytest.mark.parametrize(
    'left, right, expected', [
        (0, 2, 1),
        (2, 5, -1),
        (0, 5, -3),
    ]
                        )
def test_sumRange(left, right, expected):
    assert sol.sumRange(left, right) == expected
