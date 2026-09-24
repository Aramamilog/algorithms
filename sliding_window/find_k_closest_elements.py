from typing import List


# TODO:
#  - не очень понятно
# https://leetcode.com/problems/find-k-closest-elements/description/
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - k

        while l < r:
            m = l + (r - l) // 2

            if x - arr[m] > arr[m + k]- x:
                l = m + 1
            else:
                r = m

        return arr[l:l + k]


sol = Solution()
assert sol.findClosestElements([1,2,3,4,5], 4, 3) == [1,2,3,4]
assert sol.findClosestElements([1,1,2,3,4,5], 4, -1) == [1,1,2,3]
# time complexity O(logn)
# memory complexity O(1)
