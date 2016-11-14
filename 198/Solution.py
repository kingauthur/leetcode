class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])

        money1 = nums[0]
        money2 = max(nums[0],nums[1])

        for i in range(2,len(nums)):
            maxMoney = max(money2,money1 + nums[i])
            money1 = money2
            money2 = maxMoney

        return money2

solution = Solution()
print(solution.rob([0,1,5,3,2,7,6]))
