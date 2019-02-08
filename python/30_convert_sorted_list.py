"""
Question:
Given a singly linked list where elements are sorted in ascending order,
convert it to a height balanced BST.
Hint:
Things get a little more complicated when you have a singly linked list
instead of an array. Please note that in linked list, you no longer have
random access to an element in O(1) time.
How about inserting nodes following the list’s order? If we can achieve
this, we no longer need to find the middle element, as we are able to
traverse the list while inserting nodes to the tree.
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        pass

