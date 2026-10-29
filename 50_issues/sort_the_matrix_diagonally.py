import pytest

from collections import defaultdict


# https://leetcode.com/problems/sort-the-matrix-diagonally/description/
class Solution:
    def diagonalSort(self, mat: list[list[int]]) -> list[list[int]]:
        rows, cols = len(mat), len(mat[0])
        diagonals = defaultdict(list)

        for row in range(rows):
            for col in range(cols):
                key = row - col
                diagonals[key].append(mat[row][col])

        for v in diagonals.values():
            v.sort(reverse=True)

        for row in range(rows):
            for col in range(cols):
                key = row - col
                mat[row][col] = diagonals[key].pop()

        return mat


sol = Solution()
# time complexity O(mn*log(mn))
# Each element belongs to exactly one diagonal.
# The longest diagonal has at most min(m, n) elements.
# Sorting all diagonals takes O(m * n * log(min(m, n) + 1)).

# memory complexity O(mn)


@pytest.mark.parametrize(
    "mat, expected",
    [
        ([[3,3,1,1],[2,2,1,2],[1,1,1,2]], [[1,1,1,1],[1,2,2,2],[1,2,3,3]]),
        ([
             [11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]
         ],
         [
             [5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66],[84,28,75,33,55,68]
         ]
        )
    ]
)
def test_diagonalSort(mat, expected):
    assert sol.diagonalSort(mat) == expected
