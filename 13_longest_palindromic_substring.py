"""
Given a string s, find the longest palindromic substring in s. You may assume
that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""


class NaiveSolution:
    # TODO
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        i, j = 0, 2
        result = ""
        max_len = 0
        while j < len(s):
            substring = s[i:j]
            if substring == substring[::-1] and len(substring) > max_len:
                result = substring
                max_len = len(result)
                j += 1
            else:
                i += 1
        return result


class Solution:
    # TODO


if __name__ == "__main__":
    sol = NaiveSolution()
    print(sol.longestPalindrome("jkbsgawww"))
    print(sol.longestPalindrome(""))
    print(sol.longestPalindrome("ababbabababa"))
