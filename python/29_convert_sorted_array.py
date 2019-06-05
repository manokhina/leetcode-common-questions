"""
Question:
Given an array where elements are sorted in ascending order, convert it
to a height balanced BST.
Hint:
This question is highly recursive in nature. Think of how binary search works.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: 'List[int]') -> TreeNode:
        if not nums:
            return None

        mid = len(nums) // 2
        head = TreeNode(nums[mid])
        head.left = self.sortedArrayToBST(nums[:mid])
        head.right = self.sortedArrayToBST(nums[mid + 1:])
        return head
