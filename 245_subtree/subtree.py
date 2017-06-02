# coding:utf-8
'''
@Copyright:LintCode
@Author:   CodeWTKH
@Problem:  http://www.lintcode.com/problem/subtree
@Language: Python
@Datetime: 17-06-01 17:05
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @param T1, T2: The roots of binary tree.
    # @return: True if T2 is a subtree of T1, or false.
    def isSubtree(self, T1, T2):
        # write your code here
        if not T1 and not T2:
            return True
        if not T1 and T2:
            return False
        if T1 and not T2:
            return True
        if T1.val == T2.val:
            if self.isSameTree(T1.left, T2.left) and self.isSameTree(T1.right, T2.right):
                return True
        return self.isSubtree(T1.left, T2) or self.isSubtree(T1.right, T2)
            
    def isSameTree(self, T1, T2):
        if not T1 and not T2:
            return True
        if T1 and T2 and T1.val == T2.val:
            if self.isSameTree(T1.left, T2.left) and self.isSameTree(T1. right, T2.right):
                return True
        return False