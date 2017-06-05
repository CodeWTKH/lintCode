# coding:utf-8
'''
@Copyright:LintCode
@Author:   CodeWTKH
@Problem:  http://www.lintcode.com/problem/two-sum
@Language: Python
@Datetime: 17-06-05 06:36
'''

class Solution:
    """
    @param numbers : An array of Integer
    @param target : target = numbers[index1] + numbers[index2]
    @return : [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        d = dict()
        for i in range(len(numbers)):
            if not d.has_key(numbers[i]):
                d[target - numbers[i]] = i + 1
            else:
                return [d[numbers[i]], i+1]
        return