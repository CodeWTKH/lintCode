# coding:utf-8
'''
@Copyright:LintCode
@Author:   CodeWTKH
@Problem:  http://www.lintcode.com/problem/search-a-2d-matrix-ii
@Language: Python
@Datetime: 17-05-31 11:27
'''

class Solution:
    """
    @param matrix: An list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicates the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if len(matrix) == 0:
            return 0
        ri = list(range(len(matrix[0])))
        ci = list(range(len(matrix)))
        count = 0
        for r in ri:
            if matrix[0][r] > target:
                ri.remove(r)
        for c in ci:
            if matrix[c][0] > target:
                ci.remove(c)
        for r in ri:
            for c in ci:
                if matrix[c][r] == target:
                    count = count + 1
        return count
