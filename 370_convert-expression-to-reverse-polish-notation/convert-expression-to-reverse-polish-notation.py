# coding:utf-8
'''
@Copyright:LintCode
@Author:   CodeWTKH
@Problem:  http://www.lintcode.com/problem/convert-expression-to-reverse-polish-notation
@Language: Python
@Datetime: 17-06-03 06:27
'''

class Solution:
    # @param expression: A string list
    # @return: The Reverse Polish notation of this expression
    def convertToRPN(self, expression):
        # write your code here
        r = []
        o = []
        for c in expression:
            if c not in ('(', ')', '+', '-', '*', '/'):
                r.append(c)
            elif not o:
                o.append(c)
            elif c == '(':
                o.append(c)
            elif c == ')':
                while o[-1] != '(':
                    r.append(o.pop())
                o.pop()
            elif self.level(o[-1]) >= self.level(c):
                while o and self.level(o[-1]) >= self.level(c):
                    r.append(o.pop())
                o.append(c)
            else:
                o.append(c)
        while len(o):
            r.append(o.pop())
        return r
        
        
    def level(self, c):
        lv1 = ('(', ')')
        lv2 = ('-', '+')
        lv3 = ('*', '/', '%')
        if c in lv1:
            lv = 1
        elif c in lv2:
            lv = 2
        else:
            lv = 3
        return lv