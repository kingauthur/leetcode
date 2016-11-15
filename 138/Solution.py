# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        nodes = []
        nodesWithIndex = {}

        if head == None:
            return None

        index = 0
        pointer = head
        while pointer != None:
            node = RandomListNode(pointer.label)
            nodes.append(node)
            nodesWithIndex[pointer] = index
            index += 1
            pointer = pointer.next

        index = 0
        pointer = head
        while pointer.next != None:
            nodes[index].next = nodes[index+1]
            nodes[index].random = None if pointer.random == None   else nodes[nodesWithIndex[pointer.random]]
            index += 1
            pointer = pointer.next


        #last one
        nodes[-1].next = None
        nodes[-1].random = None if pointer.random == None else nodes[nodesWithIndex[pointer.random]]

        return nodes[0]


node = RandomListNode(1)
node.next = None
node.random = node
solution = Solution()
print(solution.copyRandomList(node))
