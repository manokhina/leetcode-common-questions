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


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 0:
            return ''

        n = len(s)
        dp = [[False for i in range(n)] for j in range(n)]
        for i in range(n):
            dp[i][i] = True
        ans = s[0:1]
        for i in range(n):
            for j in range(i - 1, -1, -1):
                if s[i] == s[j] and (i - j < 2 or dp[j + 1][i - 1]):
                    dp[j][i] = True
                    if i - j + 1 > len(ans):
                        ans = s[j:i + 1]
        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestPalindrome("jkbsgawww"))
    print(sol.longestPalindrome(""))
    print(sol.longestPalindrome("ababbabababa"))
