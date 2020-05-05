# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack_l1 = self.stack_list(l1)
        stack_l2 = self.stack_list(l2)
        
        n = self.get_num_from_stack(stack_l1, stack_l2)
        
        if n == 0:
            return ListNode(0)

        stack_l = []
        while n:
            node = ListNode(n % 10)
            stack_l.append(node)
            n = n // 10

        head = stack_l[-1]
        node = head
        for i in range(len(stack_l) - 2, -1, -1):
            node.next = stack_l[i]
            node = stack_l[i]
        return head
    
    def stack_list(self, l):
        stack = []
        node = l
        while node:
            stack.append(node)
            node = node.next
        return stack
    
    def get_num_from_stack(self, stack1, stack2):
        n1 = len(stack1) - 1
        n2 = len(stack2) - 1
        n = 0
        flag = 1
        while n1 >=0 or n2 >= 0:
            m = 0
            if n1 >= 0:
                m += stack1[n1].val
                n1 -= 1
            if n2 >= 0:
                m += stack2[n2].val
                n2 -= 1
            n += flag * m
            flag = flag * 10
        return n
