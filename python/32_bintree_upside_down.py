"""
Question:
Given a binary tree where all the right nodes are either leaf nodes with
a sibling (a left node that shares the same parent node) or empty, flip it
upside down and turn it into a tree where the original right nodes turned
into left leaf nodes. Return the new root.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def upsideDownBinaryTree(self, root):
        """
        :param: root
        :return: new root
        """
        p = TreeNode(root)
        parent = None
        parent_right = None
        while p is not None:
            left = p.left
            p.left = parent_right
            parent_right = p.right
            p.right = parent
            parent = p
            p = left
        return parent

