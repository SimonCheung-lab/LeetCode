# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        def _levelOrder(nodes):
            level = []
            sub_level = []
            for node in nodes:
                if node:
                    level.append(node.val)
                    sub_level += [node.left, node.right]
            if len(level):
                self.result.append(level)
                _levelOrder(sub_level)
        
        self.result = []
        _levelOrder([root])
        return self.result
