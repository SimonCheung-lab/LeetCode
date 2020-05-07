"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def _preorder(node):
            if node is None:
                return
            
            self.result.append(node.val)
            for c in node.children:
                _preorder(c)
        
        self.result = []
        _preorder(root)
        return self.result
