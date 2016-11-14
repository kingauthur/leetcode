class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for num in nums:
            result = result ^ num

        return result


solution = Solution()
print(solution.singleNumber([1,2,1,2,4,3,3]))
