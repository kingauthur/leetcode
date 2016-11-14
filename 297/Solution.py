# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return "^"

        return str(root.val) + " " + self.serialize(root.left) + " " + self.serialize(root.right)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        return self.doDeserialize(data.split())[0]

    def doDeserialize(self,data):
        if len(data) == 0 :
            return None,data

        if (data[0] == '^'):
            data.pop(0)
            return None,data

        node = TreeNode(int(data[0]))
        data.pop(0)

        resultleft = self.doDeserialize(data)
        node.left = resultleft[0]
        data = resultleft[1]
        resultright = self.doDeserialize(data)
        node.right = resultright[0]
        data = resultright[1]
        return node,data



# Your Codec object will be instantiated and called as such:
codec = Codec()
node1 = TreeNode(-1)
node2 = TreeNode(0)
node3 = TreeNode(1)
# node4 = TreeNode(4)
# node5 = TreeNode(5)
node1.left = node2
node1.right = node3
# node3.left = node4
# node3.right = node5
print(codec.serialize(node1))
#12^^34^^5^^
node = codec.deserialize('-1 0 ^ ^ 1 ^ ^')
print(codec.serialize(node))
# codec.deserialize(codec.serialize(root))
