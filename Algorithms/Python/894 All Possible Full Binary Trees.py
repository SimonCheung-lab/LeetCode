# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        def buildFBT(n):
            if n == 1:
                return [TreeNode(0)]

            ans = []
            for i in range(1, n, 2):
                # left + right = n - 1
                # leave one as root
                left = buildFBT(i)
                right = buildFBT(n - 1 - i)
                for l in left:
                    for r in right:
                        root = TreeNode(0)
                        root.left = l
                        root.right = r
                        ans.append(root)
            return ans

        if N % 2 == 0:
            return []

        return buildFBT(N)

    
# solution 2    
class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        def buildFBT(n):
            if n not in cache:
                ans = []
                for i in range(1, n, 2):
                    left = buildFBT(i)
                    right = buildFBT(n - 1 - i)
                    for l in left:
                        for r in right:
                            root = TreeNode(0)
                            root.left = l
                            root.right = r
                            ans.append(root)
                cache[n] = ans
            return cache[n]

        if N % 2 == 0:
            return []

        cache = {1:[TreeNode(0)]}
        return buildFBT(N)    
