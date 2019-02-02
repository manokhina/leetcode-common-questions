"""
Question:
Determine whether an integer is a palindrome. Do this without extra space.
Example Questions Candidate Might Ask:
Q: Does negative integer such as –1 qualify as a palindrome?
A: For the purpose of discussion here, we define negative integers as
non-palindrome.
"""


class NaiveSolution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        is_palindrome = False
        s = str(x)
        if s == s[::-1]:
            is_palindrome = True
        return is_palindrome
