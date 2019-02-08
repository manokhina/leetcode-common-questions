"""
Question:
Given an input string s, reverse the string word by word.
For example, given s = "the sky is blue", return "blue is sky the".
Example Questions Candidate Might Ask:
Q: What constitutes a word?
A: A sequence of non-space characters constitutes a word.
Q: Does tab or newline character count as space characters?
A: Assume the input does not contain any tabs or newline characters.
Q: Could the input string contain leading or trailing spaces?
A: Yes. However, your reversed string should not contain leading or trailing
spaces.
Q: How about multiple spaces between two words?
A: Reduce them to a single space in the reversed string.

Solution:
O(n) runtime, O(n) space:
One simple approach is a two-pass solution: First pass to split the string by
spaces into an array of words, then second pass to extract the words in
reversed order.
We can do better in one-pass. While iterating the string in reverse order,
we keep track of a word’s begin and end position. When we are at the beginning
of a word, we append it.
"""


class NaiveSolution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(s.split()[::-1])


class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        j = len(s)
        reversed_str = ""
        for i in reversed(range(len(s))):
            if s[i] == " ":
                j = i
            elif i == 0 or s[i - 1] == " ":
                if len(reversed_str) != 0:
                    reversed_str += " "
                    reversed_str += s[i:j]
        return reversed_str


if __name__ == "__main__":
    sol1 = NaiveSolution()
    sol2 = Solution()

    print(sol1.reverseWords("the sky is blue"))
    print(sol2.reverseWords("the sky is blue"))
