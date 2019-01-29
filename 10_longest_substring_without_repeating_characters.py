"""
Question:
Given a string, find the length of the longest substring without repeating
characters. For example, the longest substring without repeating letters for
“abcabcbb” is “abc”, which the length is 3. For “bbbbb” the longest substring
is “b”, with the length of 1.
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        used_char = {}
        i, length = 0, 0
        for j in range(len(s)):
            if s[j] in used_char and i <= used_char[s[j]]:
                i = used_char[s[j]] + 1
            else:
                length = max(length, j - i + 1)
            used_char[s[i]] = j
        return length


if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring("abcdabcdff"))
