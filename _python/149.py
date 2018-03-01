from sys import maxint
import collections

class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

    def __repr__(self):
        return '<%s,%s>' % (self.x, self.y)

maxint = 9223372036854775807

def get_gcd(a, b):
    """greatest common divisor"""
    if b == 0:
        return a
    return get_gcd(b, a % b)

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        res = 0
        n = len(points)
        if n < 3:
            return n
        for i in xrange(n):
            record = collections.defaultdict(int)
            same_points = 1
            for j in xrange(n):
                if i == j:
                    continue
                if points[i].x == points[j].x and points[i].y == points[j].y:
                    same_points += 1
                elif points[i].x == points[j].x:
                    record[maxint] += 1
                else:
                    a = points[i].y - points[j].y
                    b = points[i].x - points[j].x

                    gcd = get_gcd(a, b)
                    slope_fraction = (a / gcd, b / gcd)
                    record[slope_fraction] += 1
            local_max = max(record.values()) if record else 0
            local_max += same_points
            res = max(local_max, res)
        return res





if __name__ == '__main__':
    from random import randint

    points = [Point(randint(-10, 11), randint(-10, 11))
              for _ in xrange(20)]
    points = [Point(0, 0), Point(94911151, 94911150),
              Point(94911152, 94911151)]
    print points
    print Solution().maxPoints(points)
