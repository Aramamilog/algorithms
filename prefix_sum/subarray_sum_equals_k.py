from typing import List


# https://leetcode.com/problems/subarray-sum-equals-k/
# TODO: study how this algo works again and do it yourself
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # time O(n)
        # memory O(n)

        res = 0
        cur_sum = 0
        prefix_sums = {0: 1}

        for n in nums:
            cur_sum += n
            diff = cur_sum - k

            res += prefix_sums.get(diff, 0)
            prefix_sums[cur_sum] = 1 + prefix_sums.get(cur_sum, 0)

        return res
