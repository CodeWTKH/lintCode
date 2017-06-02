# coding:utf-8
'''
@Copyright:LintCode
@Author:   CodeWTKH
@Problem:  http://www.lintcode.com/problem/clone-binary-tree
@Language: Python
@Datetime: 17-06-01 18:20
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    """
    @param {TreeNode} root: The root of binary tree
    @return {TreeNode} root of new tree
    """
    def cloneTree(self, root):
        # Write your code here
        if not root:
            return None
        if not root.left and not root.right:
            return TreeNode(root.val)
        head = TreeNode(root.val)
        if root.left:
            head.left = self.cloneTree(root.left)
        if root.right:
            head.right = self.cloneTree(root.right)
        return head