# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root == None:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1




root = TreeNode(1)
left = TreeNode(2)
root.left = left
solution = Solution()
print(solution.maxDepth(root))
