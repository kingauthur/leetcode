# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
import gc
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        else:
            pointerA,pointerB = headA,headB
            diff = 0
            while pointerA.next != None:
                diff += 1
                pointerA = pointerA.next
            while pointerB.next != None:
                diff -= 1
                pointerB = pointerB.next

            if pointerA != pointerB:
                return None

            pointerA,pointerB = headA,headB

            if diff > 0:
                while diff > 0:
                    pointerA = pointerA.next
                    diff -= 1
            else:
                while diff < 0:
                    pointerB = pointerB.next
                    diff += 1

            while pointerA != None and pointerB != None:
                if pointerA == pointerB:
                    gc.collect()
                    return pointerA

                pointerA = pointerA.next
                pointerB = pointerB.next

node1 = ListNode(1)
node2 = ListNode(3)
node3 = ListNode(5)
node4 = ListNode(7)
node1.next = node2
node2.next = node3
node3.next = node4

node5 = ListNode(2)
node5.next = node4
solution = Solution()
print(solution.getIntersectionNode(node1,node5))
