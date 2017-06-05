# coding:utf-8
'''
@Copyright:LintCode
@Author:   CodeWTKH
@Problem:  http://www.lintcode.com/problem/spiral-matrix
@Language: Python
@Datetime: 17-06-04 18:08
'''

class Solution:
    # @param {int[][]} matrix a matrix of m x n elements
    # @return {int[]} an integer array
    def spiralOrder(self, matrix):
        # Write your code here
        if not matrix:
            return []
        i = m = 0
        j = len(matrix)
        if j == 1:
            return matrix[0]
        n = len(matrix[0])
        r = []
        while i < j and m < n:
            for x in range(m, n):
                r.append(matrix[i][x])
            i += 1
            for y in range(i, j):
                r.append(matrix[y][n - 1])
            n -= 1
            if i < j:
                for x in reversed(range(m, n)):
                    r.append(matrix[j - 1][x])
                j -= 1
            if m < n:
                for y in reversed(range(i, j)):
                    r.append(matrix[y][m])
                m += 1
        return r