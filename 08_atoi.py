"""
Question:
Implement atoi to convert a string to an integer.
The atoi function first discards as many whitespace characters as necessary
until the first non-whitespace character is found. Then, starting from this
character, takes an optional initial plus or minus sign followed by as many
numerical digits as possible, and interprets them as a numerical value.
The string can contain additional characters after those that form the integral
number, which are ignored and have no effect on the behavior of this function.
If the first sequence of non-whitespace characters in str is not a valid
integral number, or if no such sequence exists because either str is empty or
it contains only whitespace characters, no conversion is performed.
If no valid conversion could be performed, a zero value is returned. If the
correct value is out of the range of representable values, the maximum integer
value (2147483647) or the minimum integer value (–2147483648) is returned.
"""


class Solution:

    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        max_num = 2147483647
        min_num = -2147483648
        i, n = 0, len(str)
        sign = 1
        while i < n and str[i] == " ":
            sign = 1
            if i < n and str[i] == "+":
                i += 1
            elif i < n and str[i] == "-":
                sign = -1
                i += 1
        num = 0
        while i < n and str[i].isdigit():
            digit = int(str[i])
            if num > max_num or num == max_num and digit >= 8:
                if sign == 1:
                    return max_num
                else:
                    return min_num
            num = num * 10 + digit
            i += 1
        return sign * num
