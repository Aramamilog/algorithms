from typing import List

import pytest


# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
class Solution:

    @staticmethod
    def lower_bound(nums: List[int], target: int) -> int:
        l, r = 0, len(nums)

        while l < r:
            mid = l + (r - l) // 2

            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1

        return l if nums[l] == target else -1

    @staticmethod
    def upper_bound(nums: List[int], target: int) -> int:
        l, r = 0, len(nums)

        while l < r:
            mid = l + (r - l) // 2

            if nums[mid] > target:
                r = mid
            else:
                l = mid + 1

        return l

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        if len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]

        if nums[-1] < target:
            return [-1, -1]

        lower = self.lower_bound(nums=nums, target=target)
        if lower == -1:
            return [-1, -1]

        upper = self.upper_bound(nums=nums, target=target)  # upper bound classic

        return [lower, upper - 1]  #  -1 because we have to find last included target


sol = Solution()
# assert sol.searchRange([5,7,7,8,8,10], 8) == [3,4]
# assert sol.searchRange([5,7,7,8,8,10], 6) == [-1,-1]
# assert sol.searchRange([], 0) == [-1,-1]
# time complexity O(logn)
# memory complexity O(1)


@pytest.mark.parametrize(
    'nums, target, expected', [
        ([5, 7, 7, 8, 8, 10], 8, [3,4]),
        ([5, 7, 7, 8, 8, 10], 6, [-1,-1]),
        ([], 0, [-1,-1]),
    ]
)
def test_searchRange(nums, target, expected):
    assert sol.searchRange(nums, target) == expected
