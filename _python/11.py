# -*- coding: utf-8 -*-
# @Time    : 2018/1/21 下午3:44
# @Author  : wxy
# @File    : 11.py

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        l = 0
        r = len(height) - 1
        # area = min(height[l],height[r])*(r-l)
        maxArea = 0
        while l < r:
            print l,r
            lh = height[l]
            rh = height[r]
            h = lh if lh < rh else rh
            area = (r - l) * h
            if area > maxArea:
                maxArea = area
            if lh < rh:
                l += 1
            else:
                r -= 1
        return maxArea


if __name__ == '__main__':
    from random import randint

    l = [randint(0, 10) for _ in xrange(10)]
    l = [1,2]
    print l
    print Solution().maxArea(l)
