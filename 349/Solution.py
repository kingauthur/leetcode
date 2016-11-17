class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dist = {}
        result = set([])
        for e in nums1:
            dist[e] = 1
        for e in nums2:
            if e in dist:
                result.add(e)

        return list(result)

solution = Solution()
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(solution.intersection(nums1,nums2))
