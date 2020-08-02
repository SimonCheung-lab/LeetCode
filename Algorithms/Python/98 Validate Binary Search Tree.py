# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 1
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

    
# 2
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(root, minVal, maxVal):
            if root is None:
                return True

            if minVal != None and root.val <= minVal:
                return False

            if maxVal != None and root.val >= maxVal:
                return False

            return helper(root.left, minVal, root.val) and helper(root.right, root.val, maxVal)  

        return helper(root, None, None)
