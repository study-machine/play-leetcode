class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        a = -1
        c = len(nums)
        i = 0
        while i<c:
            if nums[i]<1 and i!=a:
                a+=1
                nums[i],nums[a]=nums[a],nums[i]
                i+=1
            elif nums[i]>1:
                c-=1
                nums[i],nums[c]=nums[c],nums[i]
            else:
                i+=1
            print nums




if __name__ == '__main__':
    from random import randint
    l = [randint(0, 2) for _ in xrange(10)]
    print 'before:', l
    Solution().sortColors(l)
    print 'end:', l
