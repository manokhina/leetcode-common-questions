"""
Question:
Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.
The brackets must close in the correct order, "()" and "()[]{}" are all valid
but "(]" and "([)]" are not.
Example Questions Candidate Might Ask:
Q: Is the empty string valid? A: Yes.
"""


class Solution:

    class Bracket:

        def __init__(self, bracket_type):
            self.bracket_type = bracket_type

        def match(self, char):
            if self.bracket_type == '[' and char == ']':
                return True
            if self.bracket_type == '{' and char == '}':
                return True
            if self.bracket_type == '(' and char == ')':
                return True
            return False

    def isValid(self, sequence: 'str') -> 'bool':
        stack = []
        for s in sequence:
            if s in ("[", "(", "{"):
                stack.append(Solution.Bracket(s))

            elif s in ("]", ")", "}"):
                if not stack:
                    return False

                top = stack.pop()

                if not top.match(s):
                    return False

        if not stack:
            return True
        return False


if __name__ == "__main__":
    sol = Solution()
    for s in ["()()((()))", "[(){{}[]}]", "[(]}}", "[", ""]:
        answer = sol.isValid(s)
        print(f"{s} is {answer}")
