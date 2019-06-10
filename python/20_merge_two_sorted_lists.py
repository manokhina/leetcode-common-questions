"""
Question:
Merge two sorted linked lists and return it as a new list. The new list should
be made by splicing together the nodes of the first two lists.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        dummy = ListNode(0)
        p = dummy
        while l1 and l2:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        if l1 is not None: p.next = l1
        if l2 is not None: p.next = l2
        return dummy.next
