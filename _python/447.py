class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        res = 0
        for x in xrange(n):
            _map = {}
            for y in xrange(n):
                if y == x:
                    continue

                p1 = points[x]
                p2 = points[y]
                dis = self.xyDistance(p1, p2)
                if dis in _map:
                    _map[dis] += 1
                else:
                    _map[dis] = 1
            res += sum([v * (v - 1) for v in _map.values() if v > 1])
        return res

    @staticmethod
    def xyDistancePower(p1, p2):
        return (p2[0] - p1[0])**2 + (p2[1] - p1[1])**2


if __name__ == '__main__':
    points = [[0, 0], [1, 0], [2, 0]]
    print Solution().numberOfBoomerangs(points)
