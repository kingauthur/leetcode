#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

import operator
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]

        nodes = []
        for l in lists:
             if l:
                 nodes.append(l)
        nodes.sort(key=operator.attrgetter('val'))
        #this one is slower than above
        #nodes.sort(key=lambda x: x.val)

        head = ListNode(0)
        pointer = head
        while len(nodes):
            node = nodes.pop(0)
            if node.next:
                nodes.append(node.next)
                nodes.sort(key=operator.attrgetter('val'))
            pointer.next = node
            pointer = pointer.next

        return head.next

node = ListNode(1)
lists = [None,node]
solution = Solution()
print(solution.mergeKLists(lists))
