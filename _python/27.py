class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = len(nums)
        i=0
        while i < n:
            if nums[i]==val:
                nums.pop(i)
                n-=1
            else:
                i+=1
        return len(nums)





if __name__ == '__main__':
    nums = [3,2,2 ,3]
    val = 3
    s = Solution()
    print s.removeElement(nums, val)
    print nums
