class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return 1

        number = [1,1]
        for i in range(0,n-2+1):
            summary = 0
            for j in range(0,len(number)):
                summary += number[j] * number[len(number)-1-j]
            number.append(summary)

        return number[-1]

solution = Solution()
print(solution.numTrees(100))
