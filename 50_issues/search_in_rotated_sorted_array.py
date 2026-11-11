from typing import List


# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[l]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1


sol = Solution()
assert sol.search([4,5,6,7,0,1,2], 0) == 4
assert sol.search([4,5,6,7,0,1,2], 3) == -1
assert sol.search([1], 0) == -1
# time complexity O(logn)
# memory complexity O(1)
