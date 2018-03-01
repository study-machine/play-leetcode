class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        record = dict.fromkeys(nums1,0)
        for x in nums1:
            record[x]+=1
        res = []
        for x in nums2:
            if record.get(x,0)>0:
                res.append(x)
                record[x]-=1
        return res


if __name__ == '__main__':
    n1=[1,2,2,1]
    n2=[2,2]
    print Solution().intersect(n1,n2)