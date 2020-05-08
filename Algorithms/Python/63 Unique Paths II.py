class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [1] * n
        for i in range(n):
            # encounter obstacle
            if obstacleGrid[0][i] == 1 or (i > 0 and dp[i - 1] == 0):
                dp[i] = 0
        
        for i in range(1, m):
            for j in range(n):
                if obstacleGrid[i][j] == 1 or (j == 0 and dp[j] == 0):
                    dp[j] = 0
                else:
                    if j == 0:
                        dp[j] = 1
                    else:
                        dp[j] = dp[j - 1] + dp[j]

        return dp[n - 1]
