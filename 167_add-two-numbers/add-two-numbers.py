# coding:utf-8
'''
@Copyright:LintCode
@Author:   CodeWTKH
@Problem:  http://www.lintcode.com/problem/add-two-numbers
@Language: Python
@Datetime: 17-05-31 16:58
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param l1: the first list
    # @param l2: the second list
    # @return: the sum list of l1 and l2 
    def addLists(self, l1, l2):
        # write your code here
        result = ListNode(0)
        node = result
        p = 0
        while l1 or l2:
            if l1 and l2:
                temp = l1.val + l2.val + p
                l1 = l1.next
                l2 = l2.next
            elif not l1:
                temp = l2.val + p
                l2 = l2.next
            else:
                temp = l1.val + p
                l1 = l1.next
            node.next = ListNode(temp % 10)
            p = temp // 10
            node = node.next
        if p == 1:
            node.next = ListNode(1)
        return result.next
            
            