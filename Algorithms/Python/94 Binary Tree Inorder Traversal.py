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
            
            inorder(node.left)
            self.result.append(node.val)
            inorder(node.right)
        
        self.result = []
        inorder(root)
        return self.result
