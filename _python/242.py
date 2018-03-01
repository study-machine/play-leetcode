class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = dict.fromkeys(s, 0)
        for c in s:
            d[c] += 1
        for c in t:
            if d.get(c, None):
                d[c] -= 1
            else:
                return False
        if sum(d.values())==0:
            return True
        else:
            return False


if __name__ == '__main__':
    s1 = "a"
    t1 = "ab"
    print Solution().isAnagram(s1, t1)
