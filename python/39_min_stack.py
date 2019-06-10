"""
Question:
Design a stack that supports push, pop, top, and retrieving
the minimum element in constant time.
- push(x) – Push element x onto stack.
- pop() – Removes the element on top of the stack.
- top() – Get the top element.
- getMin() – Retrieve the minimum element in the stack.
Hints:
- Consider space-time tradeoff. How would you keep track of
the minimums using extra space?
- Make sure to consider duplicate elements.
"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> None:
        self.stack.pop() if self.stack else None

    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        return min(self.stack) if self.stack else None

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
