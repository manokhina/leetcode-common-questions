"""
Question:
Given a binary tree, find the maximum path sum. The path may start and end
at any node in the tree. For example, given the below binary tree,
    1
   / \
  2  4
 / \
2  3
The highlighted path yields the maximum sum 10.
Example Questions Candidate Might Ask:
Q: What if the tree is empty?
A: Assume the tree is non-empty.

Q: How about a tree that contains only a single node?
A: Then the maximum path sum starts and ends at the same node.

Q: What if every node contains negative value?
A: Then you should return the single node value that is the least negative.

Q: Does the maximum path have to go through the root node?
A: Not necessarily. For example, the below tree yield 6 as the maximum path
sum and does not go through root.
    -5
   / \
  2  3
 / \
-1 4
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        pass

