from typing import List


# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        l, r = 0, 1
        profit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                new_profit = prices[r] - prices[l]
                profit = max(profit, new_profit)
            else:
                l = r  # because we found a new min value
            r += 1

        return profit


sol = Solution()
assert sol.maxProfit([7,1,5,3,6,4]) == 5
assert sol.maxProfit([7,6,4,3,1]) == 0
# time complexity O(len(prices))
# memory complexity O(1)
