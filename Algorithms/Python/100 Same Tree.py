# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# compare their preorder traverse sequence
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def preorder(root, ans):
            if root is None:
                ans.append(None)
                return
            
            ans.append(root.val)
            preorder(root.left, ans)
            preorder(root.right, ans)
        
        ans_p = []
        ans_q = []
        preorder(p, ans_p)
        preorder(q, ans_q)
        return ans_p == ans_q

# solution 2
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        return False
