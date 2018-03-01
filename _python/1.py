# -*- coding: utf-8 -*-
# @Time    : 2018/1/20 下午8:58
# @Author  : wxy
# @File    : 1.py

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = dict()
        for i in xrange(len(nums)):
            if d.get(target-nums[i],None)!=None:
                return [d[target-nums[i]],i]
            d[nums[i]]=i




if __name__ == '__main__':
    l = [2, 7,11,15]
    t = 9
    print Solution().twoSum(l, t)
