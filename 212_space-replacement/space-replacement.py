# coding:utf-8
'''
@Copyright:LintCode
@Author:   CodeWTKH
@Problem:  http://www.lintcode.com/problem/space-replacement
@Language: Python
@Datetime: 17-05-30 14:48
'''

class Solution:
    # @param {char[]} string: An array of Char
    # @param {int} length: The true length of the string
    # @return {int} The true length of new string
    def replaceBlank(self, string, length):
        # Write your code here
        if not string:
            return None
        for i in range(len(string)):
            if string[i] == ' ':
                string[i] = '%20'
        return len(string)