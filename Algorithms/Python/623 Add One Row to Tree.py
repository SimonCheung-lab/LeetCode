# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            node = TreeNode(v)
            node.left = root
            return node
        
        self.add_value_at(root, 1, v, d)
        return root
    
    def add_value_at(self, node, D, v, d):
        # current depth is D
        if D + 1 == d:
            left_node = node.left
            right_node = node.right
            new_left_node = TreeNode(v)
            new_right_node = TreeNode(v)
            node.left = new_left_node
            node.right = new_right_node
            new_left_node.left = left_node
            new_right_node.right = right_node
            return
        
        if node.left is not None:
            self.add_value_at(node.left, D + 1, v, d)

        if node.right is not None:
            self.add_value_at(node.right, D + 1, v, d)
