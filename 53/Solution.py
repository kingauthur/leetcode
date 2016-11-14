class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largestSum = [nums[0]]
        for i in range(1,len(nums)):
            curSum = largestSum[-1] + nums[i]
            largestSum.append(curSum if curSum > nums[i] else nums[i])

        return max(largestSum)

solution = Solution()
print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,1,6]))
