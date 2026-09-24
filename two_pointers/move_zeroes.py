from typing import List


# https://leetcode.com/problems/move-zeroes/
class Solution:
    def moveZeroes(self, nums: List[int]) -> list:
        """
        Do not return anything, modify nums in-place instead.
        """
        # my solution insert left side
        # i, _range = 0, 0
        # while _range < len(nums):
        #     if nums[i] == 0:
        #         nums.pop(i)
        #         nums.append(0)
        #         i -= 1
        #     i += 1
        #     _range += 1

        # second solution swap to the right side
        l, r = 0, 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1

        # return only for the assert check
        return nums


sol = Solution()
assert sol.moveZeroes([0,1,0,3,12]) == [1,3,12,0,0]
assert sol.moveZeroes([0]) == [0]
# my solution insert left side
# time complexity pop(i) works as O(n²): deleting from the middle Python's list moved every element and works itself as O(n)
# memory complexity O(1)

# second solution swap to the right side
# time complexity O(n)
# memory complexity O(1)
