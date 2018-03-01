import collections


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {}
        for i, n in enumerate(nums):
            if n in d and i - d[n] < k:
                print d
                return True
            d[n] = i
        return False


if __name__ == '__main__':
    from random import randint
    nums = [randint(0, 10) for _ in xrange(20)]
    nums = [-1,-1]
    print nums
    k = 20
    print Solution().containsNearbyDuplicate(nums, k)
