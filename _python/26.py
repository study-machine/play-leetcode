class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 0
        for i in xrange(1, len(nums)):
            if nums[i] != nums[k]:
                k += 1
                nums[k] = nums[i]
        return k+1

    def s2(self,nums):
        k = 0
        for i in xrange(len(nums)):
            if k < 1 or nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1
        return k

if __name__ == '__main__':
    nums = [1, 1, 1,2,2,2,2,2,3,4,5,5]
    print Solution().s2(nums)
    print nums
