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
        if x >= 0:
            s = str(x)
            if s == s[::-1]:
                return True
        return False


class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        number = x
        reverse = 0

        while x > 0:
            int_to_reverse = x % 10
            reverse = (reverse * 10) + int_to_reverse
            x = x // 10
        return number == reverse


if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome(121))
    print(sol.isPalindrome(1231))
