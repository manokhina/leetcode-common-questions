"""
Question:
Validate if a given string is numeric. Some examples:
"0"  true
"0.1"  true
"abc"  false
Example Questions Candidate Might Ask:
Q: How to account for whitespaces in the string?
A: When deciding if a string is numeric, ignore both leading and trailing
whitespaces.
Q: Should I ignore spaces in between numbers – such as “1 1”?
A: No, only ignore leading and trailing whitespaces. “1 1” is not numeric.
Q: If the string contains additional characters after a number, is it
considered valid?
A: No. If the string contains any non-numeric characters (excluding whitespaces
and decimal point), it is not numeric.
Q: Is it valid if a plus or minus sign appear before the number? A: Yes. “+1”
and “-1” are both numeric.
Q: Should I consider only numbers in decimal? How about numbers in other bases
such as hexadecimal (0xFF)?
A: Only consider decimal numbers. “0xFF” is not numeric.
Q: Should I consider exponent such as “1e10” as numeric?
A: No. But feel free to work on the challenge that takes exponent into
consideration. (The Online Judge problem does take exponent into account.)
"""


class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i, n = 0, len(s)
        while i < n and s[i] == " ":
            i += 1
        if i < n and (s[i] == "+" or s[i] == "-"):
            i += 1
        is_numeric = False
        while i < n and s[i].isdigit():
            i += 1
            is_numeric = True
        if i < n and s[i] == ".":
            i += 1
            while i < n and s[i].isdigit():
                i += 1
                is_numeric = True
        if is_numeric and i < n and s[i] == 'e':
            i += 1
            is_numeric = False
            if i < n and (s[i] == "+" or s[i] == "-"):
                i += 1
                while i < n and s[i].isdigit():
                    i += 1
                    is_numeric = True
        while i < n and s[i] == " ":
            i += 1
        return is_numeric and i == n

