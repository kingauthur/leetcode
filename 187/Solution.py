class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        step = 10
        dist = {}
        substrs = set([])
        for i in range(len(s)):
            end = i + step - 1
            if end >= len(s):
                break
            else:
                substr = s[i:end+1]
                if substr not in dist:
                    dist[substr] = 1
                else:
                    substrs.add(substr)
        return list(substrs)

solution = Solution()
s = "AAAAAAAAAAAA"
print(solution.findRepeatedDnaSequences(s))
