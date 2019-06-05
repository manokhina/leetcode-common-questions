"""
Question:
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as a binary tree
in which the depth of the two subtrees of every node never differs by more
than 1.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        L = self.maxDepth(root.left)
        if L == -1:
            return -1
        R = self.maxDepth(root.right)
        if R == -1:
            return -1
        return max(L, R) + 1 if abs(L - R) <= 1 else -1

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        O(n) runtime, O(n) stack space – Bottom-up recursion:
        """
        return self.maxDepth(root) != -1

