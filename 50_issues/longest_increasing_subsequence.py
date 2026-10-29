import pytest


# https://leetcode.com/problems/longest-increasing-subsequence/description/
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        LIS = [1] * len(nums)  # base case for every index, cause every num can be LIS itself

        for i in range(len(nums) - 1, -1, -1):  # go backward, cause LIS[i] depends on already computed LIS[j]
            for j in range(i, len(nums)):  # check all subsequent elements that could extend the subsequence
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
                    # LIS[i] - best for i, 1 + LIS[j] - itself plus next

        # time: O(n^2)
        # memory: O(n)
        return max(LIS)


sol = Solution()
# time complexity O(n^2)
# memory complexity O(n)

@pytest.mark.parametrize(
    "nums,expected",
    [
        ([10,9,2,5,3,7,101,18], 4),
        ([0,1,0,3,2,3], 4),
        ([7,7,7,7,7,7,7], 1)
    ]
)
def test_lengthOfLIS(nums, expected):
    assert sol.lengthOfLIS(nums) == expected
