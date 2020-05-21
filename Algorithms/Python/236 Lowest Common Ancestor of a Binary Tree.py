# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# time cost is high
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def path(node, parent=None):
            if node is None:
                return
            
            paths[node] = paths.get(parent, []) + [node]
            path(node.left, node)
            path(node.right, node)

        paths = {}
        path(root)
        
        p_path = paths[p]
        q_path = paths[q]
        ancestor = p_path[0]
        for t in zip(*[p_path, q_path]):
            v = t[0]
            for vv in t:
                if vv is not v:
                    return ancestor
            ancestor = v
        return ancestor
        
        
# solution 2        
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None or root == p or root == q:
            return root
        
        # post order
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left is None and right is None:
            return None
        
        if left and right:
            return root
        
        if left is None:
            return right
        
        # right is None
        return left        
