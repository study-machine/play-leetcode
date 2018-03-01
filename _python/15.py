class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        print nums
        i=0
        while i < len(nums):
            comple = -nums[i]
            l = i+1
            r = len(nums)-1
            while l<r:
                sm = nums[l]+nums[r]
                if sm < comple:
                    l+=1
                elif sm > comple:
                    r-=1
                else:   # sm==comple
                    n2 = nums[l]
                    n3 = nums[r]
                    res.append([nums[i],n2,n3])
                    # handle duplicate n2
                    while l<r and nums[l]==n2:
                        l+=1
                    # handle duplicate n3
                    while l<r and nums[r]==n3:
                        r-=1
            i+=1
        return res


if __name__ == '__main__':
    # S = [-1, 0, 1, 2, -1, -4]
    S = [-1,0,1,2,-1,-4]
    print Solution().threeSum(S)

# -1,-1,