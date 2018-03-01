class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = set()
        while n!=1:
            n=self.countN(n)
            if n not in s:
                s.add(n)
            else:
                return False
        return True

    @staticmethod
    def countN(n):
        res = 0
        while n != 0:
            tmp = (n % 10)**2
            res += tmp
            n = n / 10
        return res


if __name__ == '__main__':
    print Solution().isHappy(19)
