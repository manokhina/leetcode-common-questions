"""
Question:
Given an integer, convert it to a roman numeral.
Input is guaranteed to be within the range from 1 to 3999.
Hint:
What is the range of the numbers?
"""


class Solution:
    def __init__(self):
        self.values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        self.symbols =["M", "CM", "D", "CD", "C", "XC", "L",  "XL", "X",
                       "IX", "V", "IV", "I"]

    def intToRoman(self, num: 'int') -> 'str':
        i = 0
        roman = []
        while num > 0:
            k = int(num / self.values[i])
            for j in range(k):
                roman.append(self.symbols[i])
                num -= self.values[i]
            i += 1
        return "".join(roman)


if __name__ == "__main__":
    sol = Solution()
    print(sol.intToRoman(523))
    print(sol.intToRoman(4500))
