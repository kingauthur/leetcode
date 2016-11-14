# Definition for singly-linked list.
import math
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        nodes = str(self.val);
        begin = self.next;
        while begin != None:
            nodes = nodes + str(begin.val)
            begin = begin.next
        return nodes


def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """

    l1Int = 0
    l1Index = 0
    l2Int = 0
    l2Index= 0
    while l1 != None:
        print(l1Int,l1Index,l1.val)
        #l1Int = l1Int + long(math.pow(10,l1Index) * l1.val)
        l1Int = l1Int + 10**l1Index * l1.val
        l1 = l1.next
        l1Index = l1Index + 1

    print('--',l1Int)

    while l2 != None:
        l2Int = l2Int + 10**l2Index * l2.val
        l2 = l2.next
        l2Index = l2Index + 1

    l3Int = l1Int + l2Int;
    mod = l3Int % 10
    l3 = ListNode(mod)
    index = l3
    l3Int = l3Int / 10
    while l3Int != 0:
        mod = l3Int % 10
        index.next = ListNode(mod)
        index = index.next

        l3Int = l3Int / 10
    return l3


def arrayToNode(nums):
    begin  = ListNode(nums[0])
    index = begin
    for i in range(1,len(nums) - 1):
        index.next = ListNode(nums[i])
        index = index.next
    return begin

# node1 = ListNode(0)
# node1.next = ListNode(4)
# node1.next.next = ListNode(3)

# node2 = ListNode(0)
# node2.next = ListNode(6)
# node2.next.next = ListNode(6)

#print(None == None)
node1 = arrayToNode([2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,9])
node2 = arrayToNode([5,6,4,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,9,9,9,9])
print(addTwoNumbers(node1,node2))
#(42342342342342342342342L, 23, 3)
