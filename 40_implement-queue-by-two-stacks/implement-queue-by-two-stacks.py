# coding:utf-8
'''
@Copyright:LintCode
@Author:   CodeWTKH
@Problem:  http://www.lintcode.com/problem/implement-queue-by-two-stacks
@Language: Python
@Datetime: 17-05-30 15:58
'''

class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def push(self, element):
        # write your code here
        self.stack1.append(element)

    def top(self):
        # write your code here
        # return the top element
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        tmp = self.stack2[len(self.stack2) - 1]
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return tmp

    def pop(self):
        # write your code here
        # pop and return the top element
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        tmp = self.stack2.pop()
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return tmp