import pytest


# https://leetcode.com/problems/majority-element/description/
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # first decision with extra memory
        # hash_map = {}
        # for n in nums:
        #     hash_map[n] = 1 + hash_map.get(n, 0)

        # for n, count in hash_map.items():
        #     if count > len(nums) / 2:
        #         return n

        # second decision by Boyer Moore algorithm without extra memory
        res, count = 0, 0
        for n in nums:
            if count == 0:
                res = n
            if n == res:
                count += 1
            else:
                count -= 1

        # time O(n)
        # memory O(1)

        return res


sol = Solution()
# first decision
# time complexity O(n)
# memory complexity O(n)

# second decision
# time complexity O(n)
# memory complexity O(1)


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([3,2,3], 3),
        ([2,2,1,1,1,2,2], 2)
    ]
)
def test_majorityElement(nums, expected):
    assert sol.majorityElement(nums) == expected
