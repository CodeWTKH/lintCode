# coding:utf-8
'''
@Copyright:LintCode
@Author:   CodeWTKH
@Problem:  http://www.lintcode.com/problem/fast-power
@Language: Python
@Datetime: 17-06-01 15:07
'''

class Solution:
    """
    @param a, b, n: 32bit integers
    @return: An integer
    """
    def fastPower(self, a, b, n):
        # write your code here
        if n == 0:
            return 1 % b
        elif n == 1:
            return a % b
        else:
            i = n // 2
            s = self.fastPower(a, b, i) ** 2
            if n % 2:
                s = s * a
            return s % b