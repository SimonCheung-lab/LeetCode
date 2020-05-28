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

# double recursion
class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        if head is None or root is None:
            return False

        return self.explorePath(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

    def explorePath(self, node, treeNode):
        if node is None:
            return True

        if treeNode is None:
            return False

        if node.val != treeNode.val:
            return False

        return self.explorePath(node.next, treeNode.left) or self.explorePath(node.next, treeNode.right)
