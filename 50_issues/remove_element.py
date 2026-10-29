from typing import List

import pytest


# https://leetcode.com/problems/remove-element/
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # a pointer to swap there our nums[i] val

        for _, n in enumerate(nums):  # _ or index - a pointer to iterate over an array
            if n != val:
                nums[k] = n
                k += 1

        return k



sol = Solution()
# time complexity O(n)
# memory complexity O(1)


@pytest.mark.parametrize(
    "nums, val, expected",
    [
        ([3,2,2,3], 3, 2),
    ]
)
def test_removeElement(nums, val, expected):
    assert sol.removeElement(nums, val) == expected
