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


class SolutionIII:

    def partial(self, pattern):
        """ Calculate partial match table: String -> [Int]"""
        ret = [0]

        for i in range(1, len(pattern)):
            j = ret[i - 1]
            while j > 0 and pattern[j] != pattern[i]:
                j = ret[j - 1]
            ret.append(j + 1 if pattern[j] == pattern[i] else j)
        return ret

    def strStr(self, haystack, needle):
        """
        KMP search main algorithm: String -> String -> [Int]
        Return all the matching position of pattern string P in S
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0

        partial, ret, j = self.partial(needle), [], 0

        for i in range(len(haystack)):
            while j > 0 and haystack[i] != needle[j]:
                j = partial[j - 1]
            if haystack[i] == needle[j]:
                j += 1
            if j == len(needle):
                ret.append(i - (j - 1))
                j = 0

        return ret[0] if ret else -1


if __name__ == "__main__":
    sol1 = SolutionI()
    sol2 = SolutionII()
    sol3 = SolutionIII()

    print(sol1.strStr("rartarartar", "tar"))
    print(sol2.strStr("rartarartar", "tar"))
    print(sol3.strStr("rartarartar", "tr"))
