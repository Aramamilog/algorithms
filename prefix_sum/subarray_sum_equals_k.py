from typing import List


# https://leetcode.com/problems/subarray-sum-equals-k/
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        cur_sum = 0
        prefix_sums = {0: 1}

        for n in nums:
            cur_sum += n
            diff = cur_sum - k

            res += prefix_sums.get(diff, 0)
            prefix_sums[cur_sum] = 1 + prefix_sums.get(cur_sum, 0)

        return res


sol = Solution()
assert sol.subarraySum([1,1,1], 2) == 2
assert sol.subarraySum([1,2,3], 3) == 2
# time complexity O(n)
# memory complexity O(n)
