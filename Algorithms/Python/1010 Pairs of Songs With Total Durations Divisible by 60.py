class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        n = len(time)
        if n == 0:
            return 0
        
        residual = [0] * 60
        result = 0
        for i in range(n):
            residual[time[i] % 60] += 1
        
        result += residual[0] * (residual[0] - 1) // 2 + residual[30] * (residual[30] - 1) // 2
        for i in range(1, 30):
            result += residual[i] * residual[60 - i]

        return result
