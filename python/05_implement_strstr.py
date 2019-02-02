"""
Question:
Implement strstr().
Return the index of the first occurrence of needle in haystack, or -1
if needle is not part of haystack.
"""


class SolutionI:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        # elif haystack == "":
        #     return -1
        else:
            return haystack.find(needle)


class SolutionII:
    def strStr(self, haystack, needle):
        """
        Brute-force (O(nm))
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0

        for i in range(len(haystack) - len(needle) + 1):
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    break
                if j == len(needle) - 1:
                    return i

        return -1


# class SolutionIII:
#     def strStr(self, haystack, needle):
#         """
#         KMP
#         :type haystack: str
#         :type needle: str
#         :rtype: int
#         """
