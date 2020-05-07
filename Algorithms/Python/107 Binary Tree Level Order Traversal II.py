# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        def _levelOrder(nodes):
            if len(nodes) == 0:
                return

            level = []
            sub_level = []
            for node in nodes:
                if node:
                    level.append(node.val)
                    sub_level += [node.left, node.right]
            
            _levelOrder(sub_level)
            if len(level):
                self.result.append(level)

        self.result = []
        _levelOrder([root])
        return self.result
