# coding:utf-8
'''
@Copyright:LintCode
@Author:   CodeWTKH
@Problem:  http://www.lintcode.com/problem/reverse-linked-list
@Language: Python
@Datetime: 17-05-31 11:58
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
    @param head: The first node of the linked list.
    @return: You should return the head of the reversed linked list. 
                  Reverse it in-place.
    """
    def reverse(self, head):
        # write your code here
        if not head:
            return None
        next = head.next
        head.next = None
        while next:
            next.next, head, next = head, next, next.next
        return head