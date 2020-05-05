# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        # in order traverse
        def in_order_traverse(node):
            if node is None:
                return
            
            in_order_traverse(node.left)
            if k - node.val in self.cache:
                self.result = True
                return
            else:
                self.cache[node.val] = self.i
                self.i += 1
            in_order_traverse(node.right)

        self.i = 0
        self.cache = {}
        self.result = False
        in_order_traverse(root)
        return self.result
