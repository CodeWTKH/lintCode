# coding:utf-8
'''
@Copyright:LintCode
@Author:   CodeWTKH
@Problem:  http://www.lintcode.com/problem/binary-tree-preorder-traversal
@Language: Python
@Datetime: 17-06-02 06:16
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of binary tree.
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        # write your code here
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        preOrder = [root.val]
        if root.left:
            preOrder.extend(self.preorderTraversal(root.left))
        if root.right:
            preOrder.extend(self.preorderTraversal(root.right))
        return preOrder