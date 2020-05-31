class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def dfs(start, target):
            if len(path) == k and target == 0:
                ans.append(path[:])
                return
            
            if len(path) < k and target > 0:
                for i in range(start, 10):
                    path.append(i)
                    dfs(i + 1, target - i)
                    path.pop()
            
        ans = []
        path = []
        dfs(1, n)
        return ans
