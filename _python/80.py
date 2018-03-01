class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        k = 0
        a = 0
        for i in xrange(1, len(nums)):
            if nums[i] == nums[k] and a == 0:
                k += 1
                a = 1
                nums[k] = nums[i]
            if nums[i] != nums[k]:
                k += 1
                nums[k] = nums[i]
                a = 0
        return k + 1

    def s2(self, nums):
        k = 0
        for i in xrange(len(nums)):
            if k < 2 or nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1
        return k


if __name__ == '__main__':
    from random import randint
    l = sorted([randint(1, 3) for _ in xrange(10)])
    print l
    print Solution().s2(l)
    print l
