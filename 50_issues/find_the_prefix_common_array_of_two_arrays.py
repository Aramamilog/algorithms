from typing import List

import pytest


# https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        set_a = set()
        set_b = set()
        both_set = set()
        result = []

        for i in range(len(A)):
            set_a.add(A[i])
            set_b.add(B[i])
            if A[i] in set_b:
                both_set.add(A[i])
            if B[i] in set_a:
                both_set.add(B[i])
            result.append(len(both_set))

        return result


sol = Solution()
# time complexity O(n)
# memory complexity O(n) + O(n) + O(n) = O(3n) = O(n)


@pytest.mark.parametrize(
    "A, B, expected",
    [
        ([1,3,2,4], [3,1,2,4], [0,2,3,4]),
        ([2,3,1], [3,1,2], [0,1,3])
    ]
)
def test_findThePrefixCommonArray(A, B, expected):
    assert sol.findThePrefixCommonArray(A, B) == expected
