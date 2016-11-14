# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self,head):
        if head == None:
            return False

        fast = head
        slow = head

        while fast != None and slow != None:
            if fast.next == None or slow.next == None:
                return False

            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True

        return False

    # def hasCycle(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: bool
    #     """
    #     if head == None:
    #         return False
    #
    #     ori = head
    #     head = head.next
    #
    #     while head != None:
    #         if head == ori:
    #             return True
    #         head = head.next
    #
    #     return False

node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(4)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node1
solution = Solution()
print(solution.hasCycle(node1))
