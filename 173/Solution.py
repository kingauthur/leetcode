# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        self.stack = []
        while root != None:
            self.stack.append(root)
            root = root.left


    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) != 0


    def next(self):
        """
        :rtype: int
        """
        smallest = self.stack.pop(-1);
        if smallest.right != None:
            node = smallest.right
            while node != None:
                self.stack.append(node)
                node = node.left
        return smallest.val





# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
