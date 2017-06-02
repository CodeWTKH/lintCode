# coding:utf-8
'''
@Copyright:LintCode
@Author:   CodeWTKH
@Problem:  http://www.lintcode.com/problem/singleton
@Language: Python
@Datetime: 17-05-30 14:45
'''

class Solution:
    # @return: The same instance of this class every time
    @classmethod
    def getInstance(cls):
        # write your code here
        if not hasattr(cls, '_instance'):  
            cls._instance = cls() 
        return cls._instance 