from typing import List


# TODO:
#  - почему в итоге делаем l, r = 0, len(nums), а не l, r = 0, len(nums) - 1
#  - все ли краевые случаи должны быть обработаны в явном виде или алгоритм должен пройти их сам?
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
class Solution:
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

        def lower_bound():
            l, r = 0, len(nums)

            while l < r:
                mid = l + (r - l) // 2

                if nums[mid] >= target:
                    r = mid
                else:
                    l = mid + 1

            return l if nums[l] == target else -1

        lower = lower_bound()
        if lower == -1:
            return [-1, -1]

        def upper_bound():
            l, r = 0, len(nums)

            while l < r:
                mid = l + (r - l) // 2

                if nums[mid] > target:
                    r = mid
                else:
                    l = mid + 1

            return l

        upper = upper_bound()  # upper bound classic

        return [lower, upper - 1]  #  -1 because we have to find last included target


sol = Solution()
assert sol.searchRange([5,7,7,8,8,10], 8) == [3,4]
assert sol.searchRange([5,7,7,8,8,10], 6) == [-1,-1]
assert sol.searchRange([], 0) == [-1,-1]
# time complexity O(logn)
# memory complexity O(1)
