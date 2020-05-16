# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# get the specific shape of tree
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def generate(start, end):
            if start > end:
                return [None]
            
            trees = []
            for i in range(start, end + 1):
                # bulid left tree
                left_tree = generate(start, i - 1)
                # build right tree
                right_tree = generate(i + 1, end)

                # choose i as the root
                for lt in left_tree:
                    for rt in right_tree:
                        root = TreeNode(i)
                        root.left = lt
                        root.right = rt
                        trees.append(root)
            return trees

        return generate(1, n) if n else []                                                 
