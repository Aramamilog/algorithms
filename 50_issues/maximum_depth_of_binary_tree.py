import collections
from typing import Optional

import pytest


# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        level = 0

        # bfs algorithm
        q = collections.deque()
        q.append(root)

        while q:
            for i in range(len(q)):  # run through the level
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1

        return level



sol = Solution()
# time complexity O(n)
# memory complexity O(n)


@pytest.mark.parametrize(
    "root, expected",
    [
        (
            TreeNode(
                3,
                left=TreeNode(9),
                right=TreeNode(
                    20,
                    left=TreeNode(15),
                    right=TreeNode(7),
                ),
            ),
            3,
        ),
        (TreeNode(1), 1),
        (None, 0),
    ],
)
def test_maxDepth(root, expected):
    assert Solution().maxDepth(root) == expected
