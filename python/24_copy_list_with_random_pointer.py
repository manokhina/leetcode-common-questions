"""
Question:
A linked list is given such that each node contains an additional random
pointer that could point to any node in the list or null.
Return a deep copy of the list.
"""


class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        map = {None: None}
        temp = head
        while temp:
            map[temp] = Node(temp.val, temp.next, temp.random)
            temp = temp.next
        temp = head
        while temp:
            map[temp].next = map[temp.next]
            map[temp].random = map[temp.random]
            temp = temp.next
        return map[head]
