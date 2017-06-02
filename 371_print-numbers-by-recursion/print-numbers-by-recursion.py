# coding:utf-8
'''
@Copyright:LintCode
@Author:   CodeWTKH
@Problem:  http://www.lintcode.com/problem/print-numbers-by-recursion
@Language: Python
@Datetime: 17-06-01 15:12
'''

class Solution:
    # @param n: An integer.
    # return : A list of integer storing 1 to the largest number with n digits.
    def numbersByRecursion(self, n):
        # write your code here
        i = 1
        while n:
            i *= 10
            n -=1
        return range(1, i)