class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        first = 0
        second = 0
        while(second <= (len(nums) - 1) and first <= (len(nums) - 1)):
            if nums[second] == 0:
                second += 1
            elif nums[first] != 0:
                first += 1
                # this is very important, wo should replace zero to the last
                # 我们是要把zero和后面的数字去换
                second = first
            else:
                temp = nums[first]
                nums[first] = nums[second]
                nums[second] = temp
                second += 1
                first += 1


solution = Solution()
print(solution.moveZeroes([4,2,4,0,0,3,0,5,1,0]))
