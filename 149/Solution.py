class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if(len(points) == 1):
            return 1

        maxPoints = 0
        for i in range(len(points)):
            dist = {}
            same = 0
            for j in range(len(points)):
                if i == j:
                    continue

                if points[i].x == points[j].x and points[i].y == points[j].y:
                    same += 1
                    continue
                elif points[i].x == points[j].x:
                    key = "INF"
                else:
                    key = (points[j].y - points[i].y) * 1.0 / (points[j].x - points[i].x)

                if key not in dist:
                    dist[key] = 1
                else:
                    dist[key] += 1

            maxPointsEach = (0 if len(dist.values()) == 0 else max(dist.values())) + same + 1  #1 is the node itself

            if maxPointsEach > maxPoints:
                maxPoints = maxPointsEach

        return maxPoints

p1 = Point(1,1)
p2 = Point(1,1)
p3 = Point(3,3)
p4 = Point(3,3)
solution = Solution()
print(solution.maxPoints([p1,p2,p3,p4]))
