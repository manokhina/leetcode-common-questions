"""
Question:
Given a string S, find the length of the longest substring T that contains at
most two distinct characters.
For example,
Given S = “eceba”,
T is "ece" which its length is 3.
"""


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        i, j, max_len = 0, -1, 0
        for k in range(1, len(s)):
            if s[k] == s[k - 1]:
                continue
            if j >= 0 and s[j] != s[k]:
                max_len = max(k - i, max_len)
                i = j + 1
            j = k - 1
        return max(len(s) - i, max_len)


if __name__ == "__main__":
    solution = Solution()
    s = "eceba"
    print(s)
    print(solution.lengthOfLongestSubstringTwoDistinct(s))
