"""
Question:
Given a matrix of m ✕n elements (m rows, n columns), return all elements
of the matrix in spiral order.
For example, given the following matrix:
[
  [ 1, 2, 3 ],
  [ 4, 5, 6 ],
  [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
"""


class Solution:
    def spiralOrder(self, matrix: 'List[List[int]]') -> 'List[int]':
        elements = []
        if len(matrix) == 0:
            return elements
        m = len(matrix)
        n = len(matrix[0])
        row = 0
        col = -1
        while True:
            for i in range(n):
                col += 1
                elements.append(matrix[row][col])
            m -= 1
            if m == 0:
                break
            for i in range(m):
                row += 1
                elements.append(matrix[row][col])
            n -= 1
            if n == 0:
                break
            for i in range(n):
                col -= 1
                elements.append(matrix[row][col])
            m -= 1
            if m == 0:
                break
            for i in range(m):
                row -= 1
                elements.append(matrix[row][col])
            n -= 1
            if n == 0:
                break
        return elements
