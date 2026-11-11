import pytest


# https://leetcode.com/problems/maximize-distance-to-closest-person/description/
class Solution:
    def maxDistToClosest(self, seats: list[int]) -> int:
        last_occupied = None
        gap = 1

        for i, s in enumerate(seats):
            if s == 1 and last_occupied is None:  # corner case if first one not 1
                gap = max(gap, i)
                last_occupied = i
            elif s == 1:
                gap = max(gap, (i - last_occupied) // 2)
                last_occupied = i

        return max(gap, len(seats) - 1 - last_occupied)  # corner case if last one is 0


sol = Solution()
# time complexity O(n)
# memory complexity O(1)


@pytest.mark.parametrize(
    "seats, expected",
    [
        ([1,0,0,0,1,0,1], 2),
        ([1,0,0,0], 3),
        ([0,1], 1)
    ]
)
def test_maxDistToClosest(seats, expected):
    assert sol.maxDistToClosest(seats) == expected
