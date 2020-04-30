# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        p = head

        s = l1.val + l2.val
        p.val = s % 10
        s = s // 10

        l1 = l1.next
        l2 = l2.next

        while l1 is not None and l2 is not None:
            s = s + l1.val + l2.val
            p.next = ListNode(s % 10)
            p = p.next
            s = s // 10

            l1 = l1.next
            l2 = l2.next
        
        while l1 is not None:
            s = s + l1.val
            p.next = ListNode(s % 10)
            p = p.next
            s = s // 10 

            l1 = l1.next           

        while l2 is not None:
            s = s + l2.val
            p.next = ListNode(s % 10)
            p = p.next
            s = s // 10 

            l2 = l2.next

        if s > 0:
            p.next = ListNode(s)

        return head
