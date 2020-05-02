# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        if root is None:
            return 0

        left_sum = 0
        if root.left is not None:
            left_sum = self.sum_of_subtree(root.left) + root.left.val
        right_sum = 0;
        if root.right is not None:
            right_sum = self.sum_of_subtree(root.right) + root.right.val

        tilt = abs(left_sum - right_sum);

        return tilt + self.findTilt(root.left) + self.findTilt(root.right);      

    def sum_of_subtree(self, node):
        s = 0;
        if node.left is not None:
            s = node.left.val + self.sum_of_subtree(node.left)
        if node.right is not None:
            s = s + node.right.val + self.sum_of_subtree(node.right)
        return s;
