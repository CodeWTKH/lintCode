# coding:utf-8
'''
@Copyright:LintCode
@Author:   CodeWTKH
@Problem:  http://www.lintcode.com/problem/binary-tree-inorder-traversal
@Language: Python
@Datetime: 17-06-02 10:22
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
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        # write your code here
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        r = []
        if root.left:
            r.extend(self.inorderTraversal(root.left))
        r.append(root.val)
        if root.right:
            r.extend(self.inorderTraversal(root.right))
        return r