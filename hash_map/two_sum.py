from typing import List


# https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        # time O(n)
        # memory O(2)
        for ind, num in enumerate(nums):
            diff = target - num
            if diff in hash_map:
                return [hash_map.get(diff), ind]
            else:
                hash_map.update({num: ind})
