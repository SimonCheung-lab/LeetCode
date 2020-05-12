# solution 1, Backtracking, out of time
class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        def path(k, i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                self.result += 1
                return

            if k == N:
                return

            for direction in move.values():
                # i += direction[0]
                # j += direction[1]
                path(k + 1, i + direction[0], j + direction[1])
        
        move = {'up':(-1, 0), 'down':(1, 0), 'left':(0, -1), 'right':(0, 1)}
        self.result = 0
        path(0, i, j)
        return self.result % 1000000007
        
# solution 2
class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        cache = [{} for _ in range(N + 1)]
        cache[0][(i, j)] = 1
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        result = 0
        for step in range(1, N + 1):
            for row, col in cache[step - 1]:
                count = cache[step - 1][(row, col)]
                for r, c in directions:
                    pr, pc = row + r, col + c
                    if pr < 0 or pr >= m or pc < 0 or pc >= n:
                        result += count
                    elif (pr, pc) in cache[step]:
                        cache[step][(pr, pc)] += count
                    else:
                        cache[step][(pr, pc)] = count

        return result % 1000000007
