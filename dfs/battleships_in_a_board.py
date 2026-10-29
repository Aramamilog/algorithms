import pytest


# https://leetcode.com/problems/battleships-in-a-board/?utm_source=chatgpt.com
def count_battleships(board):
    """
    Возвращает количество кораблей на поле.

    'X' — часть корабля
    '.' — вода

    Требования:
    - O(rows * cols) времени
    - O(1) дополнительной памяти
    - не изменять board

    Пример:

    [               c
                r ["X", ".", ".", "X"],
                  [".", ".", ".", "X"],
                  [".", ".", ".", "X"],
    ]

    Ответ: 2
    """
    row, col = len(board), len(board[0])
    res = 0
    # memory O(1)
    # time O(r * c)
    for r in range(row):
        for c in range(col):
            if board[r][c] == "X" and (c == 0 or board[r][c - 1] != "X") and (r == 0 or board[r - 1][c] != "X"):
                res += 1

    return res

@pytest.mark.parametrize(
    "board, expected",
    [
        (
            [
                ["X", ".", ".", "X"],
                [".", ".", ".", "X"],
                [".", ".", ".", "X"],
            ],
            2,
        ),
        (
            [
                ["X", ".", ".", "X"],
                ["X", ".", ".", "X"],
                [".", "X", "X", "."],
            ],
            3,
        ),
    ],
)
def test_count_battleships(board, expected):
    assert count_battleships(board) == expected
