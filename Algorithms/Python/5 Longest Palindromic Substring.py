class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n  for _ in range(n)]
        start, max_len = 0, 1
        for i in range(1, n):
            for j in range(i):
                if s[j] == s[i]:
                    if i - j < 3:
                        dp[j][i] = True
                    else:
                        dp[j][i] = dp[j + 1][i - 1]
                
                if dp[j][i] and i - j + 1 > max_len:
                    start = j
                    max_len = i - j + 1

        return s[start: start + max_len]
