class Solution(object):
    def __init__(self):
        self.dist = {}


    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return 1

        if n in self.dist:
            return self.dist[n]

        start = 0
        for i in range(0,n):
            start = start + self.numTrees(i) * self.numTrees(n-1-i);

        self.dist[n] = start
        return start

solution = Solution()
print(solution.numTrees(100))
