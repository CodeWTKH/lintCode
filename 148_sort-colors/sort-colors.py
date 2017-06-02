# coding:utf-8
'''
@Copyright:LintCode
@Author:   CodeWTKH
@Problem:  http://www.lintcode.com/problem/sort-colors
@Language: Python
@Datetime: 17-06-01 19:02
'''

class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """
    def sortColors(self, nums):
        # write your code here
        if not nums:
            return None
        lo = 0
        hi = len(nums) - 1
        hi = self.quickSort(nums, 2, lo, hi)
        self.quickSort(nums, 1, lo ,hi)
        return nums
        
        
    def quickSort(self, nums, t, lo, hi):
        while lo < hi:
            while nums[lo] < t:
                lo += 1
            while nums[hi] >= t:
                hi -= 1
            if lo < hi:
                nums[lo], nums[hi] = nums[hi], nums[lo]
        return hi
                
        