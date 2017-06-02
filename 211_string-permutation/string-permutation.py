# coding:utf-8
'''
@Copyright:LintCode
@Author:   CodeWTKH
@Problem:  http://www.lintcode.com/problem/string-permutation
@Language: Python
@Datetime: 17-05-31 09:19
'''

class Solution:
    # @param {string} A a string
    # @param {string} B a string
    # @return {boolean} a boolean
    def stringPermutation(self, A, B):
        # Write your code here
        a = []
        b = []
        for c in A:
            a.append(c)
        for c in B:
            b.append(c)
        a = sorted(a)
        b = sorted(b)
        if a == b:
            return True
        else:
            return False