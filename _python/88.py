# -*- coding: utf-8 -*-
# @Time    : 2018/1/19 下午3:24
# @Author  : wxy
# @File    : 88.py


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        copy1 = nums1[:]
        p1 = 0
        p2 = 0
        for i in xrange(m + n):
            if p1 >= m:
                nums1[i] = nums2[p2]
                p2 += 1
            elif p2 >= n:
                nums1[i] = copy1[p1]
                p1 += 1
            elif copy1[p1] < nums2[p2]:
                nums1[i] = copy1[p1]
                p1 += 1
            else:
                nums1[i] = nums2[p2]
                p2 += 1
        pass


if __name__ == '__main__':
    l1 = [0]
    l2 = [1]

    Solution().merge(l1, 0, l2, len(l2))
    print l1
