"""
Question:
Given a binary tree, determine if it is a valid Binary Search Tree (BST).
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: 'TreeNode') -> 'bool':
        if root is None:
            return True
        return self.isSubtreeLessThan(root.left, root.val) and \
               self.isSubtreeGreaterThan(root.right, root.val) and \
               self.isValidBST(root.left) and self.isValidBST(root.right)

    def isSubtreeLessThan(self, p, val):
        if p is None:
            return True
        return p.val < val and self.isSubtreeLessThan(p.left, val) and \
               self.isSubtreeLessThan(p.right, val)

    def isSubtreeGreaterThan(self, p, val):
        if p is None:
            return True
        return p.val > val and self.isSubtreeGreaterThan(p.left, val) and \
               self.isSubtreeGreaterThan(p.right, val)

