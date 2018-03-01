class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for s in strs:
            k = self.strSort(s)
            d.setdefault(k, [])
            d[k].append(s)
        return d.values()

    @staticmethod
    def strSort(s):
        new_s = ''
        _hash = [0 for _ in xrange(26)]
        for c in s:
            _hash[ord(c) - 97] += 1
        for i, x in enumerate(_hash):
            if x:
                new_s += chr(i + 97) * x
        return new_s


if __name__ == '__main__':
    s = ["eat", "tea", "tan", "ate", "nat", "bat"]
    s = ["cab", "pug", "pei", "nay", "ron", "rae", "ems", "ida", "mes"]
    print Solution().groupAnagrams(s)
