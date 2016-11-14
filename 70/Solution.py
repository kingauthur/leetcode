class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2

        steps = [1,2]
        for i in range(1,n-1):
            steps.append(steps[-1] + steps[-2])

        return steps[-1]



solution = Solution()
print(solution.climbStairs(35))
