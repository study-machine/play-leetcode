class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        d = {}
        for i,n in enumerate(nums):
            if n in d[n] and 

        

if __name__ == '__main__':
    from random import randint
    nums = [randint(0, 10) for _ in xrange(20)]
    k = 5
    t = 5
    print nums
    print Solution().containsDuplicate(nums)
