from typing import List

import pytest


# https://leetcode.com/problems/remove-element/
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # a pointer to swap there our nums[i] val

        for n in nums:
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
        ([3, 2, 2, 3], 3, [2, 2]),
        ([0, 1, 2, 2, 3, 0, 4, 2], 2, [0, 1, 3, 0, 4]),
        ([1, 1, 1], 1, []),
        ([1, 2, 3], 4, [1, 2, 3]),
        ([5], 5, []),
        ([5], 3, [5]),
        ([], 1, []),
    ],
)
def test_removeElement(nums, val, expected):
    k = sol.removeElement(nums, val)

    assert k == len(expected)
    assert nums[:k] == expected
