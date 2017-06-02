# coding:utf-8
'''
@Copyright:LintCode
@Author:   CodeWTKH
@Problem:  http://www.lintcode.com/problem/linked-list-cycle-ii
@Language: Python
@Datetime: 17-06-01 08:28
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
    @return: The node where the cycle begins. 
                if there is no cycle, return null
    """
    def detectCycle(self, head):
        # write your code here
        low = head
        fast = head
        while fast and fast.next:
            low = low.next
            fast = fast.next.next
            if low is fast:
                fast = head
                while True:
                    fast = fast.next
                    low = low.next
                    if fast is low:
                        return fast
        return None
