from typing import List

import pytest


# https://leetcode.com/problems/partition-labels/
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {c: i for i, c in enumerate(s)}

        result = []
        size = 0
        end = 0
        for i, c in enumerate(s):
            size += 1
            end = max(end, last_index[c])
            if i == end:
                result.append(size)
                size = 0

        return result



sol = Solution()
# time complexity O(n)
# memory complexity O(n)


@pytest.mark.parametrize(
    "s, expected",
    [
        ("ababcbacadefegdehijhklij", [9,7,8]),
    ]
)
def test_partitionLabels(s, expected):
    assert sol.partitionLabels(s) == expected
