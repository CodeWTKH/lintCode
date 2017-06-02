# coding:utf-8
'''
@Copyright:LintCode
@Author:   CodeWTKH
@Problem:  http://www.lintcode.com/problem/two-sum-input-array-is-sorted
@Language: Python
@Datetime: 17-05-31 09:05
'''

class Solution:
    """
    @param nums {int[]} n array of Integer
    @param target {int} = nums[index1] + nums[index2]
    @return {int[]} [index1 + 1, index2 + 1] (index1 < index2)
    """
    def bi_serch(self, lo, nums, target):
        lo = 0
        hi = len(nums) - 1
        while hi >= lo:
            mi = lo + (hi - lo) // 2
            if nums[mi] < target:
                lo = mi + 1
            elif nums[mi] > target:
                hi = mi - 1
            else:
                return mi
        return -1
        
        
    def twoSum(self, nums, target):
        # Write your code here
        for i in range(len(nums)):
            t = target - nums[i]
            i2 = self.bi_serch(t+1, nums, t)
            if i2 != -1:
                return [i+1, i2+1]
        return