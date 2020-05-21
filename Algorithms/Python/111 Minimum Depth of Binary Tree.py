# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        if root.left is None and root.right is None:
            return 1

        left_depth = float('inf')
        right_depth = float('inf')
        if root.left:
            left_depth = self.minDepth(root.left)

        if root.right:
            right_depth = self.minDepth(root.right)

        return min(left_depth, right_depth) + 1
        
        
# depth first        
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        stack, min_depth = [(root, 1)], float('inf')
        while stack:
            node, depth = stack.pop()
            children = [node.left, node.right]
            if not any(children):
                min_depth = min(min_depth, depth)
            for child in children:
                if child:
                    stack.append((child, depth + 1))

        return min_depth        
