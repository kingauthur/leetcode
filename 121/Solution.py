class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
            
        maxProfit = 0
        minPrice = prices[0]
        for i in range(1,len(prices)):
            minPrice = min(minPrice,prices[i])
            maxProfit = max(maxProfit,prices[i] - minPrice)

        return maxProfit

solution = Solution()
print(solution.maxProfit([7, 6, 4, 3, 1]))
