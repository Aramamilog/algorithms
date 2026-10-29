import pytest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# https://leetcode.com/problems/validate-binary-search-tree/
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        if not root:
            return True

        def dfs(node, left, right):
            if not node:
                return True

            if not (left < node.val < right):
                return False

            return dfs(node.left, left, node.val) and dfs(node.right, node.val, right)

        return dfs(root, float("-inf"), float("inf"))


sol = Solution()
# time complexity O(n) + O(n) = O(2n) = O(n)
# memory complexity O(stack(dfs))

root_node = TreeNode(5,
                     TreeNode(4, None, None),
                     TreeNode(6,
                              TreeNode(3, None, None),
                              TreeNode(8, None, None)
                              )
                     )

root_node_2 = TreeNode(2,
                     TreeNode(1, None, None),
                     TreeNode(3, None, None),
                     )

@pytest.mark.parametrize(
    "root, expected",
    [
        (root_node, False),
        (root_node_2, True),
     ]
)
def test_isValidBST(root, expected):
    assert sol.isValidBST(root) == expected
