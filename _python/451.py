class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = dict()
        for c in s:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1

        x = ['' for _ in xrange(len(s)+1)]
        for k,v in d.items():
            x[v]+=k*v
        res=''
        for i in xrange(len(s),-1,-1):
            if x[i]:
                res+=x[i]
        return res


if __name__ == '__main__':
    # s = 'tree'
    s = 'eeeee'
    print Solution().frequencySort(s)
