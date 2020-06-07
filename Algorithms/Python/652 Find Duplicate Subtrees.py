# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        def serialize(node):
            if not node:
                return '#'
            
            key = str(node.val) + ',' + serialize(node.left) + ',' + serialize(node.right)
            cache[key] = cache.get(key, 0) + 1
            if cache[key] == 2:
                ans.append(node)

            return key
        
        ans = []
        cache = {}
        serialize(root)
        return ans
