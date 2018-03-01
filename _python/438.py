class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        _hash = [0 for _ in range(256)]
        for x in p:
            _hash[ord(x)] += 1
        left = 0
        right = 0
        count = len(p)
        while right < len(s):
            if _hash[ord(s[right])] >= 1:
                count-=1
            _hash[ord(s[right])] -= 1
            right += 1
            if count == 0:
                res.append(left)
            if right - left == len(p): 
                if _hash[ord(s[left])] >= 0:
                    count+=1
                _hash[ord(s[left])] += 1
                left += 1
        return res


if __name__ == '__main__':
    s = "cbaebabacd"
    p = "abc"
    print Solution().findAnagrams(s, p)
