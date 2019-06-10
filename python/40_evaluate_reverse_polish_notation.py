"""
Question:
Evaluate the value of an arithmetic expression in Reverse Polish Notation.
Valid operators are +, -, *, /. Each operand may be an integer or another
expression. Some examples:
["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9 ["4", "13", "5", "/", "+"] ->
-> (4 + (13 / 5)) -> 6
Example Questions Candidate Might Ask:
Q: Is an empty array a valid input?
A: No.
"""


class Solution:
    OPERATORS = {"+", "-", "*", "/"}

    def evalRPN(self, tokens: 'List[str]') -> int:
        stack = []
        for token in tokens:
            if token in Solution.OPERATORS:
                y = stack.pop()
                x = stack.pop()
                stack.append(self.eval(x, y, token))
            else:
                stack.append(int(token))
        return stack.pop()

    def eval(self, x, y, operator) -> int:
        if operator == "+":
            return x + y
        elif operator == "*":
            return x * y
        elif operator == "-":
            return x - y
        else:
            return int(x / y)


if __name__ == "__main__":
    sol = Solution()
    print(sol.evalRPN(["4", "13", "5", "/", "+"]))
    print(sol.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*",
                       "17", "+", "5", "+"]))
