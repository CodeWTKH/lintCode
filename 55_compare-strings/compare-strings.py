# coding:utf-8
'''
@Copyright:LintCode
@Author:   CodeWTKH
@Problem:  http://www.lintcode.com/problem/compare-strings
@Language: Python
@Datetime: 17-05-30 20:10
'''

class Solution:
    """
    @param A : A string includes Upper Case letters
    @param B : A string includes Upper Case letters
    @return :  if string A contains all of the characters in B return True else return False
    """
    def compareStrings(self, A, B):
        # write your code here
        if not A and B:
            return False
        a = []
        for c in A:
            a.append(c)
        for c in B:
            for i in range(len(a)):
                if a[i] == c:
                    a[i] = '.'
                    break
                if i == len(a) - 1:
                    return False
        return True