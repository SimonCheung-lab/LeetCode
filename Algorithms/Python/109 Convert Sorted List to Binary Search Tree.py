# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def bulid_tree(left, right):
            if left > right:
                return None

            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = bulid_tree(left, mid - 1)
            root.right = bulid_tree(mid + 1, right)
            return root

        nums = []
        node = head
        while node:
            nums.append(node.val)
            node = node.next
        return bulid_tree(0, len(nums) - 1)
