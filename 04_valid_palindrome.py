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
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pattern = re.compile('[^a-zA-Z0-9]')
        s = pattern.sub('', s.lower())
        return s == s[::-1]

    def isPalindrome2(self, s):
        """
        Two pointers solution
        :type s: str
        :rtype: bool
        """
        pattern = re.compile('[^a-zA-Z0-9]')
        s = pattern.sub('', s.lower())
        if s == "":
            return True
        else:
            left, right = 0, len(s) - 1
            while left < right:
                if s[left] != s[right]:
                    return False
                else:
                    left += 1
                    right -= 1
            return True
