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


# https://leetcode.com/problems/valid-anagram/
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # first decision
        # if s and t consist of lowercase English letters
        # time O(len(s/t))
        # memory O(52)
        # count_s = [0] * 26
        # count_t = [0] * 26
        # for s_char, t_char in zip(s, t):
        #     s_index = ord(s_char) - ord('a')
        #     t_index = ord(t_char) - ord('a')

        #     count_s[s_index] +=1
        #     count_t[t_index] +=1

        # return count_s == count_t

        # second decision
        # time O(len(s/t))
        # memory O(s) + O(t) = O(c)
        count_s = {}
        count_t = {}
        for i in range(len(s)):
            count_s[s[i]] = count_s.get(s[i], 0) + 1
            count_t[t[i]] = count_t.get(t[i], 0) + 1
        for i in count_s:
            if count_s[i] != count_t.get(i, 0):
                return False

        return True


# https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        # time O(s)
        # memory O(s)
        stack = []
        close_to_open = {
            ')': '(',
            '}': '{',
            ']': '[',
        }

        for c in s:
            if c in close_to_open:
                if stack and close_to_open[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return not stack # corner case for a "({[" input


# https://leetcode.com/problems/isomorphic-strings/
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # time O(len(s/t)) = O(n)
        # memory O(len(s)+len(t)) = O(2n) = O(n)
        hash_map_s = {}
        hash_map_t = {}
        for sc, tc in zip(s, t):
            if sc in hash_map_s:
                if hash_map_s[sc] != tc:
                    return False

            elif tc in hash_map_t:
                if hash_map_t[tc] != sc:
                    return False

            else:
                hash_map_s[sc] = tc
                hash_map_t[tc] = sc

        return True



# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # time O(len(prices))
        # memory O(c)
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


# https://leetcode.com/problems/move-zeroes/
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # time O(n)
        # memory O(1)

        # my solution insert left side
        # i, _range = 0, 0
        # while _range < len(nums):
        #     if nums[i] == 0:
        #         nums.pop(i)
        #         nums.append(0)
        #         i -= 1
        #     i += 1
        #     _range += 1

        # second solution swap to the rigth side
        l, r = 0, 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1


# https://leetcode.com/problems/squares-of-a-sorted-array/
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # time O(n)
        # memory O(n)

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
