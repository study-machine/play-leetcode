# -*- coding: utf-8 -*-
# @Time    : 2018/1/21 下午1:33
# @Author  : wxy
# @File    : 125.py


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        p1 = 0
        p2 = len(s) - 1
        while p1 < p2:
            # c1 = s[p1]
            # c2 = s[p2]
            if self.is_alpha_numeric(s[p1]) and self.is_alpha_numeric(s[p2]):
                if s[p1] == s[p2]:
                    p1 += 1
                    p2 -= 1
                elif s[p1].lower() == s[p2].lower():
                    p1 += 1
                    p2 -= 1
                else:
                    return False
            if not self.is_alpha_numeric(s[p1]):
                p1 += 1
            if not self.is_alpha_numeric(s[p2]):
                p2 -= 1

        return True

    @staticmethod
    def is_alpha_numeric(c):
        # ascii
        # A-Z   65-90
        # a-z   97-122
        # 0-9   48-57
        return 48 <= ord(c) <= 57 or 65 <= ord(c) <= 90 or 97 <= ord(c) <= 122


if __name__ == '__main__':
    s1 = "A man, a plan, a canal: Panama"
    s2 = "0P"
    s3 = ",; W;:GlG:;l ;,"
    s4 ="`l;`` 1o1 ??;l`"
    # print Solution().isPalindrome(s1)
    # print Solution().isPalindrome(s2)
    # print Solution().isPalindrome(s3)
    print Solution().isPalindrome(s4)


