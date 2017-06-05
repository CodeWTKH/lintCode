# coding:utf-8
'''
@Copyright:LintCode
@Author:   CodeWTKH
@Problem:  http://www.lintcode.com/problem/plus-one
@Language: Python
@Datetime: 17-06-05 07:54
'''

class Solution:
    # @param {int[]} digits a number represented as an array of digits
    # @return {int[]} the result
    def plusOne(self, digits):
        # Write your code here
        p = (digits[-1] + 1) // 10
        digits[-1] = (digits[-1] + 1) % 10
        i = len(digits) - 2
        while p and i >= 0:
            d = (digits[i] + p) % 10
            p = (digits[i] + p) // 10
            digits[i] = d
            i -= 1
        if p:
            digits.append(p)
            for i in range(len(digits) - 1):
                digits[len(digits) - 1], digits[i] = digits[i], digits[len(digits) - 1]
        return digits