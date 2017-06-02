# coding:utf-8
'''
@Copyright:LintCode
@Author:   CodeWTKH
@Problem:  http://www.lintcode.com/problem/partition-array-by-odd-and-even
@Language: Python
@Datetime: 17-06-01 15:41
'''

class Solution:
    # @param nums: a list of integers
    # @return: nothing
    def partitionArray(self, nums):
        # write your code here
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            while nums[lo] % 2:
                lo += 1
            while not nums[hi] % 2:
                hi -= 1
            if lo < hi:
                nums[lo], nums[hi] = nums[hi], nums[lo]
            lo += 1
            hi -= 1
        return nums
