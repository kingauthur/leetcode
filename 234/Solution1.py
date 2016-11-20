# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True

        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        cur = slow.next
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        print(prev.next)

        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next

        return True




        # if length % 2 == 0:
        #     pointer = head
        #     summary = 0
        #     index = 1
        #     while pointer:
        #         if index <= length/2:
        #             summary += pointer.val
        #         else:
        #             summary -= pointer.val
        #         pointer = pointer.next
        #     if summary == 0:
        #         return True
        #     else:
        #         return False
        # else:
        #     pointer = head
        #     summary = 0
        #     index = 1
        #     while pointer:
        #         if index <= length/2:
        #             summary += pointer.val
        #         elif index == length/2 + 1:
        #             continue
        #         else:
        #             summary -= pointer.val
        #         pointer = pointer.val
        #     if summary == 0:
        #         return True
        #     else:
        #         return False


node1 = ListNode(1)
node2 = ListNode(1)
node3 = ListNode(2)
node4 = ListNode(1)
node1.next = node2
node2.next = node3
node3.next = node4
solution = Solution()
print(solution.isPalindrome(node1))
