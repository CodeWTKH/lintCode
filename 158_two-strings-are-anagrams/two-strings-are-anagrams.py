# coding:utf-8
'''
@Copyright:LintCode
@Author:   CodeWTKH
@Problem:  http://www.lintcode.com/problem/two-strings-are-anagrams
@Language: Python
@Datetime: 17-05-30 19:51
'''

class Solution:
    """
    @param s: The first string
    @param b: The second string
    @return true or false
    """
    def anagram(self, s, t):
        # write your code here
        ls = len(s)
        lt = len(t)
        if ls != lt:
            return False
        if ls == 0:
            return True
        s = sorted(s)
        t = sorted(t)
        if s == t:
            return True
        else:
            return False