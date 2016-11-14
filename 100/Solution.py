class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        strs1 = []
        strs2 = []
        self.doConvert(p,strs1)
        self.doConvert(q,strs2)

        return strs1 == strs2

    def doConvert(self,p,strs):
        if p != None:
            strs.append(p.val)
            self.doConvert(p.left,strs)
            self.doConvert(p.right,strs)
        else:
            strs.append('#')
