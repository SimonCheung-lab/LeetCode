class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        n = len(A)
        # dp = [{}] * n  wrong!
        dp = [{} for _ in range(n)]
        max_len = 2
        for i in range(1, n):
            for j in range(i):
                diff = A[i] - A[j]
                m = dp[j].get(diff, 1) + 1
                dp[i][diff] = m
            max_len = max(max_len, max(dp[i].values()))
        return max_len
