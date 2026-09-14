from typing import List


# https://leetcode.com/problems/summary-ranges/description/
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ####################################################
        # # time complexity: O(n)
        # # memory complexity: O(n)
        ####################################################
        # def prep_result(s_list: List[int]) -> str:
        #     if len(s_list) == 1:
        #         return f"{s_list[0]}"
        #     return f"{s_list[0]}->{s_list[-1]}"
        #
        # result = []
        #
        # if not nums:
        #     return []
        #
        # if len(nums) == 1:
        #     return [f"{nums[0]}"]
        #
        # l, r = 0, 0
        # small = []
        #
        # while r < len(nums):
        #     small.append(nums[l])
        #     r += 1
        #
        #     if r < len(nums) and (nums[l] == nums[r] - 1):
        #         l += 1
        #         continue
        #     else:
        #         result.append(prep_result(small))
        #         small = []
        #         l += 1

        ####################################################
        # # time complexity: O(n)
        # # memory complexity: O(1)
        ####################################################
        def prep_result(left: int, right: int) -> str:
            if left == right:
                return f"{nums[left]}"
            return f"{nums[left]}->{nums[right]}"

        result = []
        l, r = 0, 0

        while r < len(nums):
            r += 1

            if r < len(nums) and (nums[r] - nums[r - 1] == 1):
                continue

            result.append(prep_result(left=l, right=r - 1))
            l = r


        ####################################################
        return result
