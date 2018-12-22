"""
Question:
Given a string, determine if it is a palindrome, considering only
alphanumeric characters and ignoring cases.
For example,
"A man, a plan, a canal: Panama" is a palindrome. "race a car" is not a palindrome.
Example Questions Candidate Might Ask:
Q: What about an empty string? Is it a valid palindrome?
A: For the purpose of this problem, we define empty string as valid palindrome.

"""
import re


class Solution:
    def is_palindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pattern = re.compile('[^a-zA-Z0-9]')
        s = pattern.sub('', s.lower())
        return s == s[::-1]
