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


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def sortedListToBST(self, head):
        if not head:
            return None

        root = self.helper(head)
        return root

    def helper(self, head):
        pre = None
        slow = head
        fast = head

        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next

        root = TreeNode(slow.val)

        if pre:
            pre.next = None
            left_root = self.helper(head)
            root.left = left_root
        if slow.next:
            right_root = self.helper(slow.next)
            root.right = right_root

        return root

