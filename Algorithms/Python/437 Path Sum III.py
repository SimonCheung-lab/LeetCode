# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1: Double recursion
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
        
        
# Solution 2: prefix sum + deep first search(stack)       
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.result = 0
        # statistic of prefix sums 
        cache = {0: 1}

        def dfs(node, prefix_sum):
            if node is None:
                return 
        
            prefix_sum += node.val
            self.result += cache.get(prefix_sum - sum, 0)
            cache[prefix_sum] = cache.get(prefix_sum, 0) + 1

            dfs(node.left, prefix_sum)
            dfs(node.right, prefix_sum)
            # before out the stack, remove the prefix sum of current node
            cache[prefix_sum] -= 1

        dfs(root, 0)

        return self.result
