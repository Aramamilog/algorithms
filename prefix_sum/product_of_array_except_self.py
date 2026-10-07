from typing import List

import pytest


# https://leetcode.com/problems/product-of-array-except-self/
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # result = []

        # skip_index = 0
        # while len(result) < len(nums):
        #     new_product = 1
        #     for i, num in enumerate(nums):
        #         if i == skip_index:
        #             num = 1

        #         new_product *= num

        #     result.append(new_product)
        #     skip_index += 1

        # return result

        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res


sol = Solution()
# first decision with brute forcing:
# time complexity O(n²)
# memory complexity O(n)

# second decision:
# time complexity O(n) + O(n) = O(n)
# memory complexity O(n)


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1,2,3,4], [24,12,8,6]),
        ([-1,1,0,-3,3], [0,0,9,0,0]),
    ]
)
def test_productExceptSelf(nums, expected):
    assert sol.productExceptSelf(nums) == expected
