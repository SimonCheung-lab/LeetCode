# 1
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 0:
            return 0

        n = len(triangle)
        dp = [float('inf')] * len(triangle[-1])
        dp[0] = triangle[0][0]
        for i in range(1, n):
            tmp = dp[:]
            for j in range(i + 1):
                if j == 0:
                    dp[j] = tmp[0] + triangle[i][0]
                elif j == i:
                    dp[j] = tmp[j - 1] + triangle[i][j]
                else:
                    dp[j] = min(tmp[j - 1], tmp[j]) + triangle[i][j]
        return min(dp)

    
# 2
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 0:
            return 0

        n = len(triangle)

        for i in range(n - 2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])

        return triangle[0][0]
