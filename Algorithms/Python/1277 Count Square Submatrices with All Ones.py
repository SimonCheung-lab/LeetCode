class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if len(matrix) == 0:
            return 0
        if len(matrix[0]) == 0:
            return 0

        m, n = len(matrix), len(matrix[0])
        # dp[i][j] means square so as martix[i][j] is the right down point
        dp = [[0] * n for _ in range(2)]
        result = sum(matrix[0])

        for i in range(n):
            dp[0][i] = matrix[0][i]
        
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 0:
                    dp[1][j] = 0
                else:
                    if j == 0:
                        dp[1][j] = 1
                    else:
                        dp[1][j] = min([dp[0][j - 1], dp[1][j - 1], dp[0][j]]) + 1
            # copy row 1 to row 0
            for k in range(n):
                dp[0][k] = dp[1][k]
            result += sum(dp[0])

        return result
