"""
Question:
Given a roman numeral, convert it to an integer.
Input is guaranteed to be within the range from 1 to 3999.
"""


class Solution:
    def __init__(self):
        self.symbol_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                           'D': 500, 'M': 1000}

    def romanToInt(self, s: 'str') -> 'int':
        prev = 0
        total = 0
        for c in s:
            curr = self.symbol_map[c]
            if curr > prev:
                total += curr - 2 * prev
            else:
                total += curr
            prev = curr
        return total


if __name__ == "__main__":
    sol = Solution()
    print(sol.romanToInt("DDCXI"))
    print(sol.romanToInt("CMIX"))
