from typing import Optional

import pytest


# https://leetcode.com/problems/symmetric-tree/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(l, r):
            if not l and not r:
                return True
            if not l or not r:
                return False

            return l.val == r.val and dfs(l.left, r.right) and dfs(l.right, r.left)
        return dfs(root.left, root.right)



sol = Solution()
# time complexity O(n)
# memory complexity O(h)


@pytest.mark.parametrize(
    "root, expected",
    [
        (
            TreeNode(
                1,
                left=TreeNode(
                    2,
                    left=TreeNode(3),
                    right=TreeNode(4),
                ),
                right=TreeNode(
                    2,
                    left=TreeNode(4),
                    right=TreeNode(3),
                ),
            ),
            True,
        ),
        (
            TreeNode(
                1,
                left=TreeNode(2, right=TreeNode(3)),
                right=TreeNode(2, right=TreeNode(3)),
            ),
            False,
        ),
        (TreeNode(1), True),
    ],
)
def test_isSymmetric(root, expected):
    assert Solution().isSymmetric(root) == expected
