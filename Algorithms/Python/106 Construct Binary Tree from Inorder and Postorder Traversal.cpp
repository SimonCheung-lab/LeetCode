# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) == 0:
            return None

        root = TreeNode(postorder[-1])
        if len(inorder) > 1:
            i = inorder.index(root.val)
            root.left = self.buildTree(inorder[:i], postorder[: i])
            root.right = self.buildTree(inorder[i + 1:], postorder[i: -1])

        return root
