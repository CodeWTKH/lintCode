# coding:utf-8
'''
@Copyright:LintCode
@Author:   CodeWTKH
@Problem:  http://www.lintcode.com/problem/min-stack
@Language: Python
@Datetime: 17-06-01 18:08
'''

class MinStack(object):

    def __init__(self):
        self.pq = []
        self.m = []

    def push(self, number):
        # write yout code here
        self.pq.append(number)
        if self.m:
            if self.pq[self.m[-1]] >= self.pq[-1]:
                self.m.append(len(self.pq) - 1)
        else:
            self.m.append(0)

    def pop(self):
        # pop and return the top item in stack
        if self.m[-1] == len(self.pq) - 1:
            self.m.pop()
        return self.pq.pop()

    def min(self):
        # return the mimum number in stack
        return self.pq[self.m[-1]]