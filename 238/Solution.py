class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        output = [1]
        length = len(nums)
        for i in range(1,length):
            output.append(output[-1] * nums[i-1])

        total = 1
        for i in range(1,length):
            total *= nums[length - i]
            output[length - i - 1] *= total

        return output


solution = Solution()
print(solution.productExceptSelf([1,0]))
