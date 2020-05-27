# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if len(pre) == 0:
            return None
        
        root = TreeNode(pre[0])
        if len(pre) > 1:
            # pre[1] is the root node of left
            n = post.index(pre[1]) + 1
            root.left = self.constructFromPrePost(pre[1: n + 1], post[: n])
            root.right = self.constructFromPrePost(pre[n + 1:], post[n:])
        return root
