# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1

        head = l1 if l1.val <= l2.val else l2
        p, p1, p2 = head, l1, l2
        if p1 is head:
            p1 = p1.next
        else:
            p2 = p2.next
        
        while p1 and p2:
            if p1.val <= p2.val:
                p.next = p1
                p1 = p1.next
            else:
                p.next = p2
                p2 = p2.next
            p = p.next

        if p1:
            p.next = p1
        
        if p2:
            p.next = p2

        return head
