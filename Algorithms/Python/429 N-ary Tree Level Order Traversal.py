"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        def _levelOrder(nodes):
            if len(nodes) == 0:
                return
            level = []
            childrens = []
            for node in nodes:
                if node:
                    level.append(node.val)
                    childrens = childrens + node.children
            if len(level):
                self.result.append(level)
            _levelOrder(childrens)

        self.result = []
        _levelOrder([root])
        return self.result
