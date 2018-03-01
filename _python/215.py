class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        while 1:
            p = Solution.partition(nums, l, r)
            if p == k - 1:
                return nums[p]
            if p < k - 1:
                l = p + 1
            else:  #
                r = p - 1

    @staticmethod
    def partition(arr, l, r):
        e = arr[l]
        lt = r
        gt = l + 1
        while lt >= gt:
            if arr[lt] > e and arr[gt] < e:
                Solution.swap(arr, lt, gt)
            if arr[lt] <= e:
                lt -= 1
            if arr[gt] >= e:
                gt += 1
        Solution.swap(arr, l, lt)
        return lt

    @staticmethod
    def swap(arr, x, y):
        arr[x], arr[y] = arr[y], arr[x]


if __name__ == '__main__':
    l = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 9
    l=[2,1]
    k=2
    # l=[3,2,1,5,6,4]
    # k=2
    # l = [3,3,3,3,3,3,3,3,3]
    # k = 1
    res = Solution().findKthLargest(l, k)

    print l
    print res
