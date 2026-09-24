from typing import List


# https://leetcode.com/problems/squares-of-a-sorted-array/
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        res = []
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                res.append(nums[l] * nums[l])
                l += 1
            else:
                res.append(nums[r] * nums[r])
                r -= 1

        return res[::-1]


sol = Solution()
assert sol.sortedSquares([-4,-1,0,3,10]) == [0,1,9,16,100]
assert sol.sortedSquares([-7,-3,2,3,11]) == [4,9,9,49,121]
# time complexity O(n)
# memory complexity O(n) or O(1) if we do not count result
