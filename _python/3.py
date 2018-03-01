# -*- coding: utf-8 -*-
# @Time    : 2018/1/21 下午9:21
# @Author  : wxy
# @File    : 3.py

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = {}
        l = 0
        r = -1
        max_count = 1
        while l < len(s):
            if r + 1 < len(s) and not freq.get(s[r + 1], 0):
                freq[s[r + 1]] = 1
                r += 1
            else:
                freq[s[l]] = 0
                l += 1
            count = r - l + 1
            if count > max_count:
                max_count = count

        return max_count


if __name__ == '__main__':
    s = "abcabcbb"
    s = 'pwwkew'
    s = 'c'
    s = 'au'
    # s = 'aab'
    # s = "dvdf"
    print Solution().lengthOfLongestSubstring(s)
