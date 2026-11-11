import collections
from typing import List

import pytest


# https://leetcode.com/problems/number-of-islands/
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        island = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(r, c):
            q = collections.deque()
            visit.add((r, c))
            q.append((r, c))
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc

                    not_visited = (r, c) not in visit
                    not_outside = rows > r >= 0 and cols > c >= 0
                    # also can do like this
                    # not_outside = r in range(rows) and c in range(cols)
                    if not_visited and not_outside and grid[r][c] == '1':
                        visit.add((r, c))
                        q.append((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visit:
                    bfs(r, c)
                    island += 1

        return island



sol = Solution()
# time complexity O(m*n)
# memory complexity O(m*n)


@pytest.mark.parametrize(
    "grid, expected",
    [
        (
            [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ],
            1,
        ),
        (
            [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ],
            3,
        ),
        (
            [
                ["0", "0"],
                ["0", "0"],
            ],
            0,
        ),
        (
            [["1"]],
            1,
        ),
        (
            [["0"]],
            0,
        ),
    ],
)
def test_numIslands(grid, expected):
    assert Solution().numIslands(grid) == expected
