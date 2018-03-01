# -*- coding: utf-8 -*-
# @Time    : 2018/1/20 下午9:50
# @Author  : wxy
# @File    : 167.py

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = 0
        r = len(numbers) - 1
        m = target / 2
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            if numbers[r] - m > m - numbers[l]:
                r -= 1
            else:
                l += 1


if __name__ == '__main__':
    arr = [1, 2, 7, 11, 15, 20, 30]
    t = 35
    print Solution().twoSum(arr, t)
