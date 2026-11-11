import pytest


# https://leetcode.com/problems/line-reflection/description/
# Premium or https://www.lintcode.com/problem/908/
class Solution:
    def isReflected(self, points: list[list[int]]) -> bool:
        points_set = {(x, y) for x, y in points}

        max_x = max(x for x, _ in points_set)
        min_x = min(x for x, _ in points_set)

        reflection_sum = min_x + max_x

        for x, y in points_set:
            reflected = (reflection_sum - x, y)
            if reflected not in points_set:
                return False

        return True


sol = Solution()
# time complexity O(n)
# memory complexity O(n)


@pytest.mark.parametrize(
    "points, expected",
    [
        ([[1,1],[-1,1]], True),
        ([[1,1],[-1,-1]], False),
    ]
)
def test_isReflected(points, expected):
    assert sol.isReflected(points) == expected
