# coding:utf-8
'''
@Copyright:LintCode
@Author:   CodeWTKH
@Problem:  http://www.lintcode.com/problem/climbing-stairs
@Language: Python
@Datetime: 17-06-02 20:43
'''

class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        # write your code here
        if n == 0:
            return 1
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            lo = 1
            hi = 2
            for i in range(n-3):
                lo, hi= hi, lo + hi
            return lo + hi
