from typing import List


# https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for ind, num in enumerate(nums):
            diff = target - num
            if diff in hash_map:
                return [hash_map.get(diff), ind]
            else:
                hash_map.update({num: ind})


sol = Solution()
assert sol.twoSum([2,7,11,15], 9) == [0,1]
assert sol.twoSum([3,2,4], 6) == [1,2]
assert sol.twoSum([3,3], 6) == [0,1]
# time complexity O(n)
# memory complexity O(n)
