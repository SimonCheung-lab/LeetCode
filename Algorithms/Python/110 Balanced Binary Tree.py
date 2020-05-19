# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(node):
            if node is None:
                return -1
            
            return max(height(node.left), height(node.right)) + 1
        
        if root is None:
            return True

        return abs(height(root.left) - height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)


# faster
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def is_Balanced(node):
            if node is None:
                return True, -1
            
            left_balanced, left_height = is_Balanced(node.left)
            if left_balanced is False:
                return False, 0

            right_balanced, right_height = is_Balanced(node.right)
            if right_balanced is False:
                return False, 0

            return abs(left_height - right_height) <= 1, max(left_height, right_height) + 1
        
        return is_Balanced(root)[0]
