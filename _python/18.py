class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        n = len(nums)
        nums.sort()

        i = 0
        while i < n:
            j = i + 1
            while j < n:
                complement = target - nums[i] - nums[j]
                front = j + 1
                back = n - 1
                while front < back:
                    # print i,j,front,back
                    sm = nums[front] + nums[back]
                    if sm < complement:
                        front += 1
                    elif sm > complement:
                        back -= 1
                    else:
                        quadruplet = [nums[i], nums[j],
                                      nums[front], nums[back]]
                        res.append(quadruplet)
                        while front<back and nums[front]==nums[front+1]:
                            front+=1
                        while front<back and nums[back]==nums[back-1]:
                            back-=1
                        front+=1

                while j+1<n and nums[j]==nums[j+1]:
                    j+=1
                j += 1

            while i+1<n and nums[i]==nums[i+1]:
                i+=1
            i += 1
        return res


if __name__ == '__main__':
    nums = [1, 0, -1, 0, -2, 2]
    # nums = [-3, -1, 0, 2, 4, 5]
    nums = [-3, -2, -1, 0, 0,0, 1, 2, 3]
    target = 0
    print Solution().fourSum(nums, target)
