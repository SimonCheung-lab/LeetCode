# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        node = root
        while node:
            if node.left:
                # find right most in left child
                right_most = node.left
                while right_most.right:
                    right_most = right_most.right
                
                right = node.right
                node.right = node.left
                node.left = None
                right_most.right = right
            node = node.right
