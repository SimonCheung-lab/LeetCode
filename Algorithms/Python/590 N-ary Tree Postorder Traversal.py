"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

# recursive
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def post_order(node):
            if node is None:
                return []

            for child in node.children:
                if child:
                    post_order(child)
            
            ans.append(node.val)
        
        ans = []
        post_order(root)
        return ans


# iterative
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        stack, ans = [root], []
        while stack:
            node = stack.pop()
            if node:
                stack += node.children
                ans.append(node.val)
        return ans[::-1]
