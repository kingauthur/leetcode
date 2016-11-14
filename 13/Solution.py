class Solution(object):

    def __init__(self):
        self.dist = {'I':1,'X':10,'C':100,'M':1000,'V':5,'L':50,'D':500}

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = self.dist[s[0]]
        for i in range(1,len(s)):
            if s[i-1] in ['I','X','C'] and self.dist[s[i]] > self.dist[s[i-1]]:
                result +=  self.dist[s[i]] - 2 * self.dist[s[i-1]]
            else:
                result += self.dist[s[i]]

        return result


solution = Solution()
print(solution.romanToInt('MCMLXXX'))
