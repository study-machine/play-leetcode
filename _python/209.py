# -*- coding: utf-8 -*-
# @Time    : 2018/1/21 下午4:22
# @Author  : wxy
# @File    : 209.py

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = -1
        tmp = 0
        m_count = len(nums) + 1
        while l < len(nums):
            print l, r
            if tmp < s and r + 1 < len(nums):
                r += 1
                tmp += nums[r]
            else:
                tmp -= nums[l]
                l += 1
            if tmp >= s and r - l + 1 < m_count:
                m_count = r - l + 1

        if m_count == len(nums) + 1:
            return 0
        return m_count


if __name__ == '__main__':
    arr = [1, 1]
    s = 3
    print Solution().minSubArrayLen(s, arr)
