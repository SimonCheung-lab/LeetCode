class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.result = []
        self.queen_position = [0] * n

        def is_ok(row, column):
            if row == 0:
                return True
            left_up = column - 1
            right_up = column + 1
            for r in range(row - 1, -1, -1):
                if self.queen_position[r] == column:
                    return False
                if 0 <= left_up == self.queen_position[r]:
                    return False
                if n > right_up == self.queen_position[r]:
                    return False
                left_up -= 1
                right_up += 1
            return True

        def n_queen(row):
            if row == n:
                # find a solution
                positions = []
                for r in range(n):
                    positions.append('.' * self.queen_position[r] + 'Q' + '.' * (n - 1 - self.queen_position[r]))
                self.result.append(positions)
                return
            
            for c in range(n):
                if is_ok(row, c):
                    self.queen_position[row] = c
                    n_queen(row + 1)

        n_queen(0)
        return self.result
