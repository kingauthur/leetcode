class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == None and t == None:
            return True
        elif s != None and t != None:
            return sorted(s) == sorted(t)
        else:
            return False

solution = Solution()
print(solution.isAnagram('anagram','nagaram'))
