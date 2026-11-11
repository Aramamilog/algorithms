import pytest


# https://leetcode.com/problems/max-consecutive-ones/
class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        res = 0
        l, r = 0, 0

        while r < len(nums):
            if nums[r] == 1:
                r += 1
            else:
                res = max(res, r - l)
                r += 1
                l = r

        return max(res, r - l)  # corner case if every nums are 1



sol = Solution()
# time complexity O(n)
# memory complexity O(1)


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1,1,0,1,1,1], 3),
        ([1,0,1,1,0,1], 2),
        ([1,1,0,1], 2)
    ]
)
def test_issueName(nums, expected):
    assert sol.findMaxConsecutiveOnes(nums) == expected
