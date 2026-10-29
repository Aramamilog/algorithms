from typing import List

import pytest


# https://link
class Solution:
    def issueName(self, s: str) -> bool:
        pass


sol = Solution()
# time complexity O(?)
# memory complexity O(?)


@pytest.mark.parametrize(
    "var, expected",
    [
        ("input value", "result value"),
    ]
)
def test_issueName(var, expected):
    assert sol.issueName(var) == expected
