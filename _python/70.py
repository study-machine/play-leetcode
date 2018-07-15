class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = [-1 for _ in range(n+1)]
        memo[0]=1
        memo[1]=1
        for i in range(2,n+1):
            memo[i]= memo[i-1]+memo[i-2]

        return memo[n]


if __name__ == '__main__':
    n = 12
    res= Solution().climbStairs(n)
    print res