class Solution(object):
    #Time Limit Exceeded
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        length = len(nums)
        result = []
        for i in range(length):
            if i and nums[i] == nums[i-1]:
                continue
            target = 0 - nums[i]
            left,right = i + 1, length - 1
            while left < right:
                if nums[left] + nums[right] == target:
                    result.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -= 1
                    # shift only we get the right one
                    while left < length and nums[left - 1] == nums[left]:
                        left += 1
                    while right < length - 2 and right >= 0 and nums[right] == nums[right + 1]:
                        right -= 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    left += 1


        return result






solution = Solution()
#print(solution.threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]))
print(solution.threeSum([-5,14,1,-2,11,11,-10,3,-6,0,3,-4,-9,-13,-8,-7,9,8,-7,11,12,-7,4,-7,-1,-5,13,1,-2,8,-13,0,-1,3,13,-13,-1,10,5,1,-13,-15,12,-7,-13,-11,-7,3,13,1,0,2,1,11,10,8,-8,1,-14,-3,-6,-12,12,0,6,2,2,-9,-3,14,-1,-9,14,-4,-1,8,-8,7,-4,12,-14,3,-9,2,0,-13,-13,-1,3,-12,11,4,-9,8,11,5,-5,-10,3,-1,-11,-13,5,-12,-10,11,11,-3,-5,14,-13,-4,-5,-7,6,2,-13,0,8,-3,4,4,-14,2]))
#print(solution.threeSum([-2,0,0,2,2]))
