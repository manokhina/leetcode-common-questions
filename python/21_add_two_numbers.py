"""
Question:
You are given two linked lists representing two non-negative numbers.
The digits are stored in reverse order and each of their nodes contains
a single digit. Add the two numbers and return it as a linked list.
Input: (2->4->3) + (5->6->4) Output: 708
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        dummy = ListNode(0)
        p = l1
        q = l2
        curr = dummy
        carry = 0
        while p or q:
            x = p.val if p is not None else 0
            y = q.val if q is not None else 0
            digit = carry + x + y
            carry = digit // 10
            curr.next = ListNode(digit % 10)
            curr = curr.next
            if p is not None: p = p.next
            if q is not None: q = q.next
        if carry > 0:
            curr.next = ListNode(carry)
        return dummy.next
