# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def preorder(node):
            if node is None:
                return

            self.result.append(node.val)
            preorder(node.left)
            preorder(node.right)
        
        self.result = []
        preorder(root)
        return self.result
