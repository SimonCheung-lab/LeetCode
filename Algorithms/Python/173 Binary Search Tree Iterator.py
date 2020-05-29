# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import queue

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.data = queue.Queue()
        self.inorder(root)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        return self.data.get()


    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return not self.data.empty()

    def inorder(self, root):
        if root is None:
            return

        self.inorder(root.left)
        self.data.put(root.val)
        self.inorder(root.right)

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

# solution 2, esentially same as solution 1
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.data = []
        self.index = -1
        self.inorder(root)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        self.index += 1
        return self.data[self.index]

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.index < len(self.data) - 1

    def inorder(self, root):
        if root is None:
            return

        self.inorder(root.left)
        self.data.append(root.val)
        self.inorder(root.right)

# solution 3        
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.left_most(root)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        node = self.stack.pop()
        self.left_most(node.right)
        return node.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0

    def left_most(self, node):
        while node:
            self.stack.append(node)
            node = node.left        
