class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(start, target):
            if target == 0:
                ans.append(path[:])
                return

            for i in range(start, len(candidates)):
                if target - candidates[i] >= 0:
                    if i > start and candidates[i] == candidates[i - 1]:
                        continue
                    path.append(candidates[i])
                    dfs(i + 1, target - candidates[i])
                    path.pop()
        
        candidates.sort()
        path = []
        ans = []
        dfs(0, target)
        return ans
