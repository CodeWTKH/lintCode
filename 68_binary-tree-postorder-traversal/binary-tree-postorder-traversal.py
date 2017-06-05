# coding:utf-8
'''
@Copyright:LintCode
@Author:   CodeWTKH
@Problem:  http://www.lintcode.com/problem/binary-tree-postorder-traversal
@Language: Python
@Datetime: 17-06-02 12:10
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
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        # write your code here
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        r = []
        if root.left:
            r.extend(self.postorderTraversal(root.left))
        if root.right:
            r.extend(self.postorderTraversal(root.right))
        r.append(root.val)
        return r