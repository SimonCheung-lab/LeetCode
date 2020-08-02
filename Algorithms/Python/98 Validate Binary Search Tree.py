# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def inOrder(node):
            nonlocal preNode

            if node is None:
                return True

            if not inOrder(node.left):
                return False
            
            if preNode and preNode.val >= node.val:
                return False
            
            preNode = node
            return inOrder(node.right)

        preNode = None

        return inOrder(root)
