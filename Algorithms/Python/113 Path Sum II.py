# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if root is None:
            return []

        result = []
        self.find_path(root, sum, [], result)
        return result

    def find_path(self, node, sum, path, result):
        if node.left is None and node.right is None and sum == node.val:
            result.append(path + [node.val])
            return 

        if node.left:
            self.find_path(node.left, sum - node.val, path + [node.val], result)
        if node.right:
            self.find_path(node.right, sum - node.val, path + [node.val], result)
