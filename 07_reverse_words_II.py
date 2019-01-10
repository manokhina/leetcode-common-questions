"""
Question:
Similar to Question [6. Reverse Words in a String], but with the following
constraints:
“The input string does not contain leading or trailing spaces and the words are
always separated by a single space.”
Could you do it in-place without allocating extra space? Solution:
O(n) runtime, O(1) space – In-place reverse:
Let us indicate the ith word by wi and its reversal as wi′. Notice that when
you reverse a
word twice, you get back the original word. That is, (wi′)′ = wi.
The input string is w1 w2 ... wn. If we reverse the entire string, it becomes
wn′ ... w2′ w1′. Finally, we reverse each individual word and it becomes
wn ... w2 w1. Similarly, the same result could be reached by reversing each
individual word first, and then reverse the entire string.

Challenge 1:
Implement the two-pass solution without using the library’s split function.

Challenge 2:
Rotate an array to the right by k steps in-place without allocating extra space.
For instance, with k = 3, the array [0, 1, 2, 3, 4, 5, 6] is rotated to
[4, 5, 6, 0, 1, 2, 3].
"""


class SolutionI:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(s.split()[::-1])


class SolutionII:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = self.reverse(s, 0, len(s))
        i = 0
        for j in range(len(s)):
            if j == len(s) or s[j] == ' ':
                s = self.reverse(s, i, j)
                i = j + 1
        return s

    @staticmethod
    def reverse(s, begin, end):
        new_s = list(s)
        # print(end, begin)
        for i in range((end - begin) // 2):
            # print(i)
            temp = s[begin + i]
            new_s[begin + i] = s[end - i - 1]
            new_s[end - i - 1] = temp
            print("tmp ", temp)
            # print(''.join(new_s))
        return ''.join(new_s)


if __name__ == "__main__":
    solution1 = SolutionI()
    solution2 = SolutionII()
    s = "Lorem ipsum"
    print(s)
    print(solution1.reverseWords(s))
    print(solution2.reverseWords(s))
