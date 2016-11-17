# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None and l2 == None:
            return None
        elif l1 == None :
            return l2
        elif l2 == None:
            return l1
        else:
            head = ListNode(0)
            pointer = head
            while l1 != None and l2 != None:
                if l1.val <= l2.val:
                    pointer.next = l1
                    l1 = l1.next
                else:
                    pointer.next = l2
                    l2 = l2.next
                pointer = pointer.next
            while l1 != None:
                pointer.next = l1
                pointer = pointer.next
                l1 = l1.next
            while l2 != None:
                pointer.next = l2
                pointer = pointer.next
                l2 = l2.next

        return head.next
