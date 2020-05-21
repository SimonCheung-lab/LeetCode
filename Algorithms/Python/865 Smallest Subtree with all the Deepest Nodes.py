# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        # get the depth of each node
        def set_depth(node, parent=None):
            if node:
                node_depth[node] = node_depth.get(parent, None) + 1
                set_depth(node.left, node)
                set_depth(node.right, node)

        node_depth = {None:-1}
        set_depth(root)
        max_depth = max(node_depth.values())

        def find(node):
            if node is None or node_depth[node] == max_depth:
                return node
            
            left = find(node.left)
            right = find(node.right)
            return node if left and right else left or right

        return find(root)
