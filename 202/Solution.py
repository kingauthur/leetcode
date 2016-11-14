class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        dist = {}
        while n != 1:
            summ = sum([int(i)**2 for i in str(n)])
            if summ not in dist:
                dist[summ] = 1
            else:
                return False
            n = summ
        return True

solution = Solution()
print(solution.isHappy(19))
