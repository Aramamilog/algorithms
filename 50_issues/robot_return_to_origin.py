import pytest


# https://leetcode.com/problems/robot-return-to-origin/description/
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x, y = 0, 0

        for move in moves:
            if move == 'U':
                y += 1
            elif move == 'D':
                y -= 1
            elif move == 'L':
                x -= 1
            elif move == 'R':
                x += 1

        # time O(n)
        # memory O(1)
        return x == 0 and y == 0


sol = Solution()
# time complexity O(n)
# memory complexity O(1)


@pytest.mark.parametrize(
    "moves, expected",
    [
        ("UD", True),
        ("LL", False),
    ]
)
def test_judgeCircle(moves, expected):
    assert sol.judgeCircle(moves) == expected
