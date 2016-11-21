# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

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

        head = self.mergeLastTwo(lists[0],lists[1])

        if len(lists) > 2:
            for i in range(2,len(lists)):
                head = self.mergeLastTwo(head,lists[i])

        return head



    def mergeLastTwo(self,list1,list2):

        pointer1 = list1
        pointer2 = list2
        head = ListNode(0)
        pointer = head

        while pointer1 and pointer2:
            if pointer1.val <= pointer2.val:
                pointer.next = pointer1
                pointer1 = pointer1.next
            else:
                pointer.next = pointer2
                pointer2 = pointer2.next
            pointer = pointer.next

        if pointer1:
            pointer.next = pointer1

        if pointer2:
            pointer.next = pointer2

        return head.next
