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

        length = 0
        pointer = head
        while pointer:
            length += 1
            pointer = pointer.next

        boundary = length / 2
        prev = None
        cur = head
        while boundary:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
            boundary -= 1

        pointer1 = prev
        pointer2 = cur if length % 2 == 0 else cur.next

        while pointer1 and pointer2:
            if pointer1.val != pointer2.val:
                return False
            pointer1 = pointer1.next
            pointer2 = pointer2.next

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
node2 = ListNode(2)
node3 = ListNode(1)
node1.next = node2
node2.next = node3
solution = Solution()
print(solution.isPalindrome(node1))
