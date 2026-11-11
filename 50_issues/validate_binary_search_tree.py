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

        # FIRST DECISION OPTIMAL
        stack = [(root, float("-inf"), float("inf"))]
        while stack:
            node, left, right = stack.pop()

            if not (left < node.val < right):
                return False

            if node.left:
                stack.append((node.left, left, node.val))

            if node.right:
                stack.append((node.right, node.val, right))

        return True

        # SECOND DECISION
        def dfs(node, left, right):
            if not node:
                return True

            if not (left < node.val < right):
                return False

            return dfs(node.left, left, node.val) and dfs(node.right, node.val, right)

        return dfs(root, float("-inf"), float("inf"))


sol = Solution()
# FIRST DECISION
# time complexity O(n) + O(n) = O(2n) = O(n)
# memory complexity O(h) worse, could be O(1) for specific type of three

# SECOND DECISION
# time complexity O(n) + O(n) = O(2n) = O(n)
# memory complexity O(h)

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


# SECOND DECISION: test limit of python recursion, has to raise RecursionError
def test_isValidBST_deep_tree():
    root = TreeNode(0)
    current = root

    for value in range(1, 5000):
        current.right = TreeNode(value)
        current = current.right

    assert Solution().isValidBST(root) is True


# SECOND DECISION: test limit of python recursion, has to raise RecursionError
def test_isValidBST_deep_invalid_tree():
    root = TreeNode(0)
    current = root

    for value in range(1, 5000):
        current.right = TreeNode(value)
        current = current.right

    current.right = TreeNode(100)

    assert Solution().isValidBST(root) is False
