# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head

        oddPointer = head
        evenPointer = head.next
        evenHead = head.next

        while evenPointer != None and evenPointer.next != None:
            oddPointer.next = evenPointer.next
            oddPointer = evenPointer.next
            evenPointer.next = oddPointer.next
            evenPointer = oddPointer.next

        oddPointer.next = evenHead

        return head
