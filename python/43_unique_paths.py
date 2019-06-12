"""
Question:
A robot is located at the top-left corner of a m×n grid (marked ‘Start’ in
the diagram below). The robot can only move either down or right at any
point in time. The robot is trying to reach the bottom-right corner
of the grid (marked ‘Finish’ in the diagram below).
How many possible unique paths are there?
"""


class Solution:
    def uniquePaths(self, m: 'int', n: 'int') -> 'int':
        mat = [[0] * (n + 1) for _ in range(m + 1)]
        mat[m - 1][n] = 1
        for r in reversed(range(m)):
            for c in reversed(range(n)):
                mat[r][c] = mat[r + 1][c] + mat[r][c + 1]
        return mat[0][0]


if __name__ == "__main__":
    sol = Solution()
    print(sol.uniquePaths(3, 2))
    print(sol.uniquePaths(2, 2))
