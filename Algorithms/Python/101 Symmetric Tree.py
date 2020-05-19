# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def symmetric(left, right):
            if left is None and right is None:
                return True

            if left and right and left.val == right.val:
                return symmetric(left.left, right.right) and symmetric(left.right, right.left)

            return False

        if root is None:
            return True
        
        return symmetric(root.left, root.right)
