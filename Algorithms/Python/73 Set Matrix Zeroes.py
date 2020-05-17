# space: O(m + n), time: O(m*n)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return
        
        m, n = len(matrix), len(matrix[0])
        zero_rows = []
        zero_columns = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_rows.append(i)
                    zero_columns.append(j)

        for row in set(zero_rows):
            matrix[row] = [0] * n

        for col in set(zero_columns):
            for i in range(m):
                matrix[i][col] = 0
           
           
# space: O(1), time: O(m*n)           
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return
        
        m, n = len(matrix), len(matrix[0])
        first_row_zero = False
        for col in range(n):
            if matrix[0][col] == 0:
                first_row_zero = True
                break
        
        first_column_zero = False
        for row in range(m):
            if matrix[row][0] == 0:
                first_column_zero = True
                break
        
        for row in range(1, m):
            for col in range(1, n):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0
        
        for col in range(1, n):
            if matrix[0][col] == 0:
                for i in range(1, m):
                    matrix[i][col] = 0

        for row in range(1, m):
            if matrix[row][0] == 0:
                for j in range(1, n):
                    matrix[row][j] = 0
        
        if first_row_zero:
            matrix[0] = [0] * n

        if first_column_zero:
            for i in range(m):
                matrix[i][0] = 0
           
