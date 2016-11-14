class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dist = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key in dist:
                dist[key].append(s)
            else:
                dist[key] = [s]
        return dist.values()

solution = Solution()
print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
