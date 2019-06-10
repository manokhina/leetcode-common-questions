"""
Question:
Merge k sorted linked lists and return it as one sorted list.
Analyze and describe its complexity.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: 'List[ListNode]') -> 'ListNode':
        if not lists:
            return None
        end = len(lists) - 1
        while end > 0:
            begin = 0
            while begin < end:
                lists[begin] = self.merge2Lists(lists[begin], lists.get[end])
                begin += 1
                end -= 1
        return lists.get(0)

    def merge2Lists(self, l1, l2):
        dummyHead = ListNode(0)
        p = dummyHead
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
        return dummyHead.next
