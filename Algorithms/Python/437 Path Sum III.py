# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Double recursion
class Solution:
    result = 0
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if root is None:
            return 0

        self.dfs(root, sum)
        self.pathSum(root.left, sum)
        self.pathSum(root.right, sum)
        return self.result

    def dfs(self, node, sum):
        if node is None:
            return
        if sum == node.val:
            self.result += 1
        self.dfs(node.left, sum - node.val)
        self.dfs(node.right, sum - node.val)
