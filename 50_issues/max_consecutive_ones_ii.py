import pytest


# https://leetcode.com/problems/max-consecutive-ones-ii/description/
# Premium or https://www.geeksforgeeks.org/dsa/max-number-of-one-ii/
class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        res = 0
        zero = 0

        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                zero += 1

            while zero > 1:
                if nums[l] == 0:
                    zero -= 1
                l += 1

            res = max(res, r - l + 1)

        return res


sol = Solution()
# time complexity O(n)
# memory complexity O(1)


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([0, 1, 0, 1, 1], 4),
        ([0, 1, 0], 2)
    ]
)
def test_findMaxConsecutiveOnes(nums, expected):
    assert sol.findMaxConsecutiveOnes(nums) == expected
