class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        count = n
        for i in range(1, n):
            for j in range(i):
                if s[j] == s[i]:
                    if i - j < 3:
                        dp[j][i] = True
                    else:
                        dp[j][i] = dp[j + 1][i - 1]
                
                if dp[j][i]:
                    count += 1
                    
        return count
