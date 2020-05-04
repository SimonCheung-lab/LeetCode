class Solution:
    def totalNQueens(self, n: int) -> int:
        self.queen_position = [0] * n 
        self.result = 0

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
                self.result += 1
                return
            
            for c in range(n):
                if is_ok(row, c):
                    self.queen_position[row] = c 
                    n_queen(row + 1)

        n_queen(0)
        return self.result 
