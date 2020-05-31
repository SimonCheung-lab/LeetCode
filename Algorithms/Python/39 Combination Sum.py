class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(start, target):
            if target == 0:
                ans.append(path[:])
                return
            
            for i in range(start, len(candidates)):
                if target - candidates[i] < 0:
                    break

                path.append(candidates[i])
                dfs(i, target - candidates[i])
                path.pop()
        
        candidates.sort()
        path = []
        ans = []
        dfs(0, target)
        return ans
