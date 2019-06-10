"""
Question:
Given a linked list, swap every two adjacent nodes and return its head.
For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.
Your algorithm should use only constant space. You may not modify the values
in the list, only nodes itself can be changed.
Example Questions Candidate Might Ask:
Q: What if the number of nodes in the linked list has only odd number of nodes?
A: The last node should not be swapped.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: 'ListNode') -> 'ListNode':
        dummy = ListNode(0)
        dummy.next = head
        p = head
        prev = dummy
        while p and p.next:
            q = p.next
            r = p.next.next
            prev.next = q
            q.next = p
            p.next = r
            prev = p
            p = r
        return dummy.next


if __name__ == "__main__":
    solution = Solution()
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    print(solution.swapPairs(l1).val)
