class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        head = 0
        tail = len(height) - 1
        maxArea = 0
        while(head <= tail):
            area = (tail - head) * min(height[head],height[tail])
            if area > maxArea:
                maxArea = area
            if height[head] < height[tail]:
                head += 1
            elif height[head] > height[tail]:
                tail -= 1
            else:
                head += 1
                tail -= 1

        return maxArea


solution = Solution()
print(solution.maxArea([1,1]))
