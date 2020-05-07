# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        def _average(nodes):
            if len(nodes) == 0:
                return
            
            level = []
            sub_level = []
            for node in nodes:
                if node:
                    level.append(node.val)
                    sub_level += [node.left, node.right]
            if len(level):
                self.result.append(mean(level))
            _average(sub_level)
        
        self.result = []
        _average([root])
        return self.result
