# -*- coding: utf-8 -*-
# @Time    : 2018/1/21 下午3:25
# @Author  : wxy
# @File    : 345.py

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        s = list(s)
        p1 = 0
        p2 = len(s) - 1
        print s
        while p1 < p2:
            while p1 < p2 and s[p1] not in vowels:
                p1 += 1
            while p1 < p2 and s[p2] not in vowels:
                p2 -= 1
            s[p1], s[p2] = s[p2], s[p1]
            p1 += 1
            p2 -= 1

        return ''.join(s)


if __name__ == '__main__':
    s = "leetcode"
    r = Solution().reverseVowels(s)
    print r
