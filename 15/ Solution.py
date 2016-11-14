class Solution(object):
    #Time Limit Exceeded
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        negas = []
        zeros = []
        posis = []
        result = []
        dist = {}
        for n in nums:
            if n > 0:
                posis.append(n)
            elif n < 0:
                negas.append(n)
            else:
                zeros.append(n)

        if len(zeros) >= 3:
            result.append((0,0,0))

        if len(negas) == 0 or len(posis) == 0:
            return result

        if len(zeros) > 0:
            for n in negas:
                if abs(n) in posis >= 0:
                    arr = (n,0,abs(n))
                    if arr not in dist:
                        dist[arr] = 1
                        result.append(arr)

        for i in range(len(negas)):
            for j in range(i+1,len(negas)):
                pos = 0 - negas[i] - negas[j]
                print(negas[i],negas[j],pos)
                if pos in posis:
                    arr = (negas[i],negas[j],pos)
                    if arr not in dist:
                        dist[arr] = 1
                        result.append(arr)
        for i in range(len(posis)):
            for j in range(i+1,len(posis)):
                nega = 0 - posis[i] - posis[j]
                if nega in negas:
                    arr = (posis[i],posis[j],nega)
                    if arr not in dist:
                        dist[arr] = 1
                        result.append(arr)

        return result

solution = Solution()
#print(solution.threeSum([-1, 0, 1, 2, -1, -4]))
print(solution.threeSum([-5,14,1,-2,11,11,-10,3,-6,0,3,-4,-9,-13,-8,-7,9,8,-7,11,12,-7,4,-7,-1,-5,13,1,-2,8,-13,0,-1,3,13,-13,-1,10,5,1,-13,-15,12,-7,-13,-11,-7,3,13,1,0,2,1,11,10,8,-8,1,-14,-3,-6,-12,12,0,6,2,2,-9,-3,14,-1,-9,14,-4,-1,8,-8,7,-4,12,-14,3,-9,2,0,-13,-13,-1,3,-12,11,4,-9,8,11,5,-5,-10,3,-1,-11,-13,5,-12,-10,11,11,-3,-5,14,-13,-4,-5,-7,6,2,-13,0,8,-3,4,4,-14,2]))
