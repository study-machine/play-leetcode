class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        _map = {}
        res = 0
        for a in A:
            for b in B:
                sm = a + b
                _map.setdefault(sm, 0)
                _map[sm] += 1
        for c in C:
            for d in D:
                comp = -(c + d)
                if comp in _map:
                    res += _map[comp]
        return res


if __name__ == '__main__':
    A = [1, 2]
    B = [-2, -1]
    C = [-1, 2]
    D = [0, 2]
    print Solution().fourSumCount(A, B, C, D)
