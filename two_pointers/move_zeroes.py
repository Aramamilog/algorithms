from typing import List


# https://leetcode.com/problems/move-zeroes/
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # time O(n)
        # memory O(1)

        # my solution insert left side
        # i, _range = 0, 0
        # while _range < len(nums):
        #     if nums[i] == 0:
        #         nums.pop(i)
        #         nums.append(0)
        #         i -= 1
        #     i += 1
        #     _range += 1

        # second solution swap to the rigth side
        l, r = 0, 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
