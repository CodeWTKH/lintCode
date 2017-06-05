# coding:utf-8
'''
@Copyright:LintCode
@Author:   CodeWTKH
@Problem:  http://www.lintcode.com/problem/copy-list-with-random-pointer
@Language: Python
@Datetime: 17-06-02 12:30
'''

# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        nhead = RandomListNode(head.label)
        t = head
        n = nhead
        while t.next:
            n.next = RandomListNode(t.next.label)
            t = t.next
            n = n.next
        t = head
        n = nhead
        while t:
            n.random = t.random
            n = n.next
            t = t.next
        return nhead