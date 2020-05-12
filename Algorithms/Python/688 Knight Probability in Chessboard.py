class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        cache = [{} for _ in range(K + 1)]
        cache[0][(r, c)] = 1
        directions = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, -1), (2, 1), (-1, -2), (1, -2)]
        for step in range(1, K + 1):
            for row, col in cache[step - 1]:
                count = cache[step - 1][(row, col)]
                for _r, _c in directions:
                    nr, nc = row + _r, col + _c
                    if nr < 0 or nc < 0 or nr >= N or nc >= N:
                        # Knight out of chessboard
                        pass
                    elif (nr, nc) in cache[step]:
                        cache[step][(nr, nc)] += count
                    else:
                        cache[step][(nr, nc)] = count
                        
        return sum(cache[K].values()) / (8 ** K)
