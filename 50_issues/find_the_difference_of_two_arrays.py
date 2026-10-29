import pytest


# https://leetcode.com/problems/find-the-difference-of-two-arrays/
class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        set_1, set_2 = set(nums1), set(nums2)
        res_1, res_2 = set(), set()

        for i in set_1:
            if i not in set_2:
                res_1.add(i)

        for i in set_2:
            if i not in set_1:
                res_2.add(i)


        return [list(res_1), list(res_2)]

        # also can do like this
        # return [list(set_1 - set_2), list(set_2 - set_1)]




sol = Solution()
# time complexity O(n + m)
# memory complexity O(n + m)


@pytest.mark.parametrize(
    "nums1, nums2, expected",
    [
        ([1,2,3], [2,4,6], [[1,3],[4,6]]),
    ]
)
def test_findDifference(nums1, nums2, expected):
    assert sol.findDifference(nums1, nums2) == expected
