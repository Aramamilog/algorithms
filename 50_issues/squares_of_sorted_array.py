from typing import List


# https://leetcode.com/problems/squares-of-a-sorted-array/
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # FIRST DECISION
        # l, r = 0, len(nums) - 1
        # res = []
        # while l <= r:
        #     if abs(nums[l]) > abs(nums[r]):
        #         res.append(nums[l] * nums[l])
        #         l += 1
        #     else:
        #         res.append(nums[r] * nums[r])
        #         r -= 1
        #
        # return res[::-1]

        # SECOND DECISION
        n = len(nums)
        result = [0] * n

        left, right = 0, n - 1

        for i in range(n - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                result[i] = nums[left] ** 2
                left += 1
            else:
                result[i] = nums[right] ** 2
                right -= 1

        return result


sol = Solution()
assert sol.sortedSquares([-4,-1,0,3,10]) == [0,1,9,16,100]
assert sol.sortedSquares([-7,-3,2,3,11]) == [4,9,9,49,121]
# FIRST DECISION
# time complexity O(n)
# memory complexity O(n)

# SECOND DECISION
# time complexity O(n)
# memory complexity O(1)
