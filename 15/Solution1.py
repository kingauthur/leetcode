class Solution(object):
    #Time Limit Exceeded
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        dist = {}

        for i in range(len(nums)):
            element1 = nums[i]
            subnums = nums[:]
            subnums.pop(i)
            result = self.twoSum(subnums,0 - element1)
            for r in result:
                tmp = sorted([element1,r[0],r[1]])
                if (tmp[0],tmp[1],tmp[2]) not in dist:
                    dist[(tmp[0],tmp[1],tmp[2])] = 1

        return dist.keys()

    # use hashtabl
    def twoSum(self,nums,target):
        dist = {}
        result = []
        for i in range(len(nums)):
            dist[nums[i]] = i
        for i in range(len(nums)):
            r = target - nums[i]
            if r in dist and dist[r] != i:
                result.append((nums[i],r))

        return result




solution = Solution()
#print(solution.threeSum([-1, 0, 1, 2, -1, -4]))
print(solution.threeSum([-5,14,1,-2,11,11,-10,3,-6,0,3,-4,-9,-13,-8,-7,9,8,-7,11,12,-7,4,-7,-1,-5,13,1,-2,8,-13,0,-1,3,13,-13,-1,10,5,1,-13,-15,12,-7,-13,-11,-7,3,13,1,0,2,1,11,10,8,-8,1,-14,-3,-6,-12,12,0,6,2,2,-9,-3,14,-1,-9,14,-4,-1,8,-8,7,-4,12,-14,3,-9,2,0,-13,-13,-1,3,-12,11,4,-9,8,11,5,-5,-10,3,-1,-11,-13,5,-12,-10,11,11,-3,-5,14,-13,-4,-5,-7,6,2,-13,0,8,-3,4,4,-14,2]))
