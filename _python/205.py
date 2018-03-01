class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        d = dict()
        u = set()
        for i in range(len(s)):
            if s[i] not in d:
                if t[i] in u:
                    return False
                d[s[i]] = t[i]
                u.add(t[i])
            else:
                if d[s[i]] != t[i]:
                    return False
        return True


if __name__ == '__main__':
    s = "egg"
    t = "add"
    print Solution().isIsomorphic(s, t)
