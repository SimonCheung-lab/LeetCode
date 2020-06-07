# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def dfs(node):
            nonlocal ans
            if not node:
                return
            
            if node.val % 2 == 0:
                if node.left:
                    if node.left.left:
                        ans += node.left.left.val
                    if node.left.right:
                        ans += node.left.right.val
                if node.right:
                    if node.right.left:
                        ans += node.right.left.val
                    if node.right.right:
                        ans += node.right.right.val                    

            dfs(node.left)
            dfs(node.right)
        
        ans = 0
        dfs(root)
        return ans
