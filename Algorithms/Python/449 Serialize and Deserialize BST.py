# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return '#'

        return str(root.val) + '(' + self.serialize(root.left) + ')(' + self.serialize(root.right) + ')'

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if data == '#':
            return None

        i = 0
        n = len(data)
        i = data.index('(')
        val = int(data[:i])
        root = TreeNode(val)

        # find left
        i += 1
        start = i
        left_parenthesis = 1
        while i < n:
            if data[i] == '(':
                left_parenthesis += 1
            elif data[i] == ')':
                left_parenthesis -= 1
            if left_parenthesis == 0:
                break
            i += 1
        left = self.deserialize(data[start: i])

        # find right
        i += 2
        start = i
        left_parenthesis = 1
        while i < n:
            if data[i] == '(':
                left_parenthesis += 1
            elif data[i] == ')':
                left_parenthesis -= 1
            if left_parenthesis == 0:
                break
            i += 1
        right = self.deserialize(data[start: i])

        root.left = left
        root.right = right
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
