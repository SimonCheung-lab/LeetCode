# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        def preorder(node):
            if not node:
                return None
            
            left = preorder(node.left)
            right = preorder(node.right)

            ans = str(node.val)

            if right:
                if left:
                    ans += '(' + left + ')' + '(' + right + ')'
                else:
                    ans += '()' + '(' + right + ')'
            else:
                if left:
                    ans += '(' + left + ')'

            return ans

        ans = preorder(t)
        return ans if ans else ''
