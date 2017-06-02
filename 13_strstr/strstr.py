# coding:utf-8
'''
@Copyright:LintCode
@Author:   CodeWTKH
@Problem:  http://www.lintcode.com/problem/strstr
@Language: Python
@Datetime: 17-05-30 14:08
'''

class Solution:
    """
    @param: : source string to be scanned.
    @param: : target string containing the sequence of characters to match
    @return: a index to the first occurrence of target in source, or -1  if target is not part of source.
    """

    def strStr(self, source, target):
        # write your code here
        if source == None or target == None:
            return -1
        ls = len(source)
        lt = len(target)
        if lt == 0:
            return 0
        for s in range(ls):
            i = s
            for t in range(lt):
                if source[i] != target[t]:
                    break
                i = i + 1
            if i == s + lt:
                return s
        return -1