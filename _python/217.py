class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums)!=len(set(nums))

        

if __name__ == '__main__':
    from random import randint
    nums = [randint(0, 10) for _ in xrange(20)]
    print nums
    print Solution().containsDuplicate(nums)
