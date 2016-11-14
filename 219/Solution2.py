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
    carry = 0
    head = ListNode(0)
    point = head
    while l1 != None and l2 != None:
        sum = carry + l1.val + l2.val
        point.next = ListNode(sum % 10)
        carry = sum / 10
        point = point.next
        l1 = l1.next
        l2 = l2.next

    while l1 != None:
        sum = carry + l1.val
        point.next = ListNode(sum % 10)
        carry = sum / 10
        point.next = point
        l1 = l1.next

    while l2 != None:
        sum = carry + l2.val
        point.next = ListNode(sum % 10)
        carry = sum / 10
        point.next = point
        l2 = l2.next

    if carry != 0:
       point.next = ListNode(carry)

    return head.next


def arrayToNode(nums):
    begin  = ListNode(nums[0])
    index = begin
    for i in range(1,len(nums) - 1):
        index.next = ListNode(nums[i])
        index = index.next
    return begin

node1 = arrayToNode([2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,9])
node2 = arrayToNode([5,6,4,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,9,9,9,9])
print(addTwoNumbers(node1,node2))
