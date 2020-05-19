# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack, ans = [root], []
        while stack:
            node = stack.pop()
            if node:
                ans.append(node.val)
                stack += [node.left, node.right]
        
        return ans[::-1]
