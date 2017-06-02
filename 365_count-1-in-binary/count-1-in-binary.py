# coding:utf-8
'''
@Copyright:LintCode
@Author:   CodeWTKH
@Problem:  http://www.lintcode.com/problem/count-1-in-binary
@Language: Python
@Datetime: 17-05-30 14:58
'''

class Solution:
    # @param num: an integer
    # @return: an integer, the number of ones in num
    def countOnes(self, num):
        # write your code here
        if num < 0:
            num = 2 ** 32 + num
        count = 0
        while num != 0:
            if num % 2 == 1:
                count = count + 1
            num = num // 2
        return count