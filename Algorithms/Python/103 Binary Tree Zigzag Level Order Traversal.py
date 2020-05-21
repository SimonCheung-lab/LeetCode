# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        def level_order(nodes, left):
            values = []
            sublevel = []
            for node in nodes:
                if node:
                    values.append(node.val)
                    sublevel += [node.left, node.right]
            
            if values:
                if not left:
                    values = values[::-1]
                ans.append(values)
            
            if sublevel:
                level_order(sublevel, not left)

        ans = []
        level_order([root], True)
        return ans
