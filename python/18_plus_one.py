"""
Given a non-empty array of digits representing a non-negative integer,
plus one to the integer.

The digits are stored such that the most significant digit is at the head
of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the
number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""


class NaiveSolution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        number = int(''.join([str(i) for i in digits])) + 1
        return [int(i) for i in str(number)]


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in reversed(range(len(digits))):
            digit = digits[i]
            if digit < 9:
                digits[i] = digit + 1
                return digits
            else:
                digits[i] = 0
        return [1] + digits


if __name__ == "__main__":
    sol = Solution()
    test_cases = [[1, 2, 3],
                  [0],
                  [9, 9, 9]]

    for test in test_cases:
        print(sol.plusOne(test))
