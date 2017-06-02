# coding:utf-8
'''
@Copyright:LintCode
@Author:   CodeWTKH
@Problem:  http://www.lintcode.com/problem/remove-nth-node-from-end-of-list
@Language: Python
@Datetime: 17-06-01 17:29
'''

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer.
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        # write your code here
        i_node = head
        t_node = head
        while n:
            t_node = t_node.next
            n -=1
        if not t_node:
            if i_node.next:
                return head.next
            else:
                return None
        while t_node.next and i_node.next:
            i_node = i_node.next
            t_node = t_node.next
        i_node.next = i_node.next.next
        return head