"""
Question:
Similar to Question [43. Unique Paths], but now consider if some obstacles are
added to the grids. How many unique paths would there be?
An obstacle and empty space are marked as 1 and 0 respectively in the grid.
"""


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: 'List[List[int]]') \
            -> 'int':
        m = len(obstacleGrid)
        if m == 0:
            return 0
        n = len(obstacleGrid[0])
        mat = [[0] * (n + 1) for _ in range(m + 1)]
        mat[m - 1][n] = 1
        for r in reversed(range(m)):
            for c in reversed(range(n)):
                mat[r][c] = 0 if obstacleGrid[r][c] == 1 else mat[r][c + 1] + \
                                                              mat[r + 1][c]
        return mat[0][0]
