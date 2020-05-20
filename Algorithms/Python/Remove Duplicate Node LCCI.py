# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        p, q = head, head.next
        values = [0] * 20001
        values[p.val] = 1
        while q:
            if values[q.val] == 0:
                values[q.val] = 1
                p.next = q
                p = q
            q = q.next
        p.next = None            
        return head
