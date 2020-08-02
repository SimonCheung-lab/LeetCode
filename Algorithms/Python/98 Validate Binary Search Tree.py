# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def inorder(node):
            nonlocal preNode
            nonlocal valid
            
            if node is None:
                return
            
            inorder(node.left)

            if preNode is None:
                preNode = node
            else:
                if preNode.val >= node.val:
                    valid = False
                    return
                else:
                    preNode = node
        
            inorder(node.right)

        preNode = None
        valid = True
        inorder(root)

        return valid
