class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dist = {}
        for e in s:
            if e in dist:
                dist[e] += 1
            else:
                dist[e] = 1

        for e in t:
            if e not in dist:
                return False
            else:
                dist[e] -= 1

        for e in dist.values():
            if e != 0:
                return False

        return True

solution = Solution()
print(solution.isAnagram('anagram','nagaram'))
