"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def connect_level(nodes):
            if len(nodes) == 0:
                return
            
            sublevel = []
            for i in range(len(nodes) - 1):
                nodes[i].next = nodes[i + 1]
                if nodes[i].left:
                    sublevel.append(nodes[i].left)
                if nodes[i].right:
                    sublevel.append(nodes[i].right)
            
            nodes[-1].next = None
            if nodes[-1].left:
                sublevel.append(nodes[-1].left)
            if nodes[-1].right:
                sublevel.append(nodes[-1].right)
            connect_level(sublevel)
        
        if root is None:
            return None

        nodes = []
        nodes.append(root)
        connect_level(nodes)
        return root


# recursion    
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root

        left, right = root.left, root.right
        while left and right:
            left.next = right
            left = left.right
            right = right.left
        
        self.connect(root.left)
        self.connect(root.right)
        return root    
