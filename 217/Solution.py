class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dist = {}
        for num in nums:
            if num in dist:
                return True
            else:
                dist[num] = 1

        return False
