# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p.val == q.val:
            return p
        elif p.val > q.val:
            return self.lowestCommonAncestor(root,q,p)
        if p.val < root.val and q.val > root.val:
            return root
        elif p.val == root.val and q.val > root.val:
            return p
        elif p.val < root.val and q.val == root.val:
            return q
        elif p.val == root.val and q.val == root.val:
            return root
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left,q,p)
        else:
            return self.lowestCommonAncestor(root.right,q,p)
