# coding:utf-8
'''
@Copyright:LintCode
@Author:   CodeWTKH
@Problem:  http://www.lintcode.com/problem/fibonacci
@Language: Python
@Datetime: 17-05-30 14:32
'''

class Solution:
    # @param n: an integer
    # @return an integer f(n)
    def fibonacci(self, n):
        # write your code here
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            lo = 0
            hi = 1
            for i in range(n-3):
                lo, hi= hi, lo + hi
            return lo + hi