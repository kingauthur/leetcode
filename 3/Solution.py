class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dist = {}
        maxLen = 0
        startIndex = 0
        for i in range(len(s)):
            char = s[i]
            if char in dist:
                lastIndex = dist[char]
                for j in range(startIndex,lastIndex + 1):
                    del dist[s[j]]
                startIndex = lastIndex + 1
            dist[char] = i
            if(len(dist) > maxLen):
                maxLen = len(dist)


        return maxLen

solution = Solution()
print(solution.lengthOfLongestSubstring("bbbbb"))
