# backtracking
class Solution:
    def countArrangement(self, N: int) -> int:
        def is_ok(i, j):
            return i % j == 0 or j % i == 0

        def arrange(i):
            if i == N + 1:
                self.result += 1
                return
            
            for j in range(1, N + 1):
                if j not in array[:min(i, N + 1)] and is_ok(i, j):
                    array[i] = j
                    arrange(i + 1)

        self.result = 0
        array = [0] * (1 + N)
        arrange(1)
        return self.result
