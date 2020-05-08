class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0:
            return 0
        if len(matrix[0]) == 0:
            return 0

        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(2)]
        max_len = 0
        for i in range(n):
            if matrix[0][i] == '1':
                dp[0][i] = 1
        max_len = max(dp[0])

        for i in range(1, m):
            for j in range(0, n):
                if matrix[i][j] == '1':
                    if j == 0:
                        dp[1][j] = 1
                    else:
                        dp[1][j] = min([dp[1][j - 1], dp[0][j], dp[0][j - 1]]) + 1
                    max_len = max([dp[1][j], max_len])
                else:
                    dp[1][j] = 0
            # copy row 1 to row 0
            for i in range(n):
                dp[0][i] = dp[1][i]
        return max_len ** 2
