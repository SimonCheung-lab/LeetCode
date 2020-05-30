# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        self.flip(root1)
        self.flip(root2)

        return self.equal(root1, root2)

    def equal(self, root1, root2):
        if root1 is None and root2 is None:
            return True

        if root1 and root2 and root1.val == root2.val:
            return self.equal(root1.left, root2.left) and self.equal(root1.right, root2.right)

        return False

    def flip(self, root):
        if root is None:
            return

        if root.right is None or (root.left and root.left.val > root.right.val):
            # swap
            node = root.left
            root.left = root.right
            root.right = node

        self.flip(root.left)
        self.flip(root.right)

        
class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        def preorder(root):
            if root:
                yield root.val
                L = root.left.val if root.left else -1
                R = root.right.val if root.right else -1
                if L < R:
                    yield from preorder(root.left)
                    yield from preorder(root.right)
                else:
                    yield from preorder(root.right)
                    yield from preorder(root.left)

        return all(x == y for x, y in itertools.zip_longest(preorder(root1), preorder(root2)))        
