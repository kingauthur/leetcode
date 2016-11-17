class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        maxRec = 0
        for i in range(len(matrix)):
            left = 0
            right = 0
            for j in range(len(matrix[i]))
