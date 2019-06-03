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
    def dfsBottomUp(self, p, parent):
        if p is None: return parent
        root = self.dfsBottomUp(p.left, p)
        if parent is None:
            p.left = parent
        else:
            p.left = parent.right
        p.right = parent
        return root

    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        return self.dfsBottomUp(root, None)


