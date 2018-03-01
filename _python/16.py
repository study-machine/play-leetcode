class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = []
        nums.sort()
        closet_low = sum(nums[:3])
        closet_high = sum(nums[-3:])

        n = len(nums)
        i = 0
        for i in xrange(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = n - 1
            while l < r:
                # print i, l, r
                sm3 = nums[i] + nums[l] + nums[r]
                if closet_low < sm3 <= target:
                    closet_low = sm3
                elif target <= sm3 < closet_high:
                    closet_high = sm3
                # print closet_low, closet_high

                if sm3 < target:
                    l += 1
                elif sm3 > target:
                    r -= 1
                else:
                    return sm3
                while l + 1 < r and nums[l] == nums[l + 1]:
                    l += 1
                while l + 1 < r and nums[r] == nums[r - 1]:
                    r -= 1
        if target - closet_low < closet_high - target:
            return closet_low
        else:
            return closet_high


if __name__ == '__main__':
    s = [0, 0, 0]
    s = [-1, -1, 1, 1, 3]
    s = [-1, 0, 1, 1, 55]

    target = 3
    print Solution().threeSumClosest(s, target)
