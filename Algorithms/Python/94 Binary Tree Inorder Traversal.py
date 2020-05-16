# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def inorder(node):
            if node is None:
                return
            
            nonlocal result
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
        
        result = []
        inorder(root)
        return self.result
