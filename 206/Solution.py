# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        preNode = None
        while(head != None):
            temp = head.next
            head.next = preNode
            preNode = head
            head = temp
        return preNode
