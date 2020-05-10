class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        
        m, n = len(matrix), len(matrix[0])
        flag = [[0] * n for _ in range(m)]
        k = 0
        row, col = 0, 0
        result = []
        count = m * n
        while k < count:
            # turn right
            while col < n and flag[row][col] == 0:
                result.append(matrix[row][col])
                flag[row][col] = 1
                col += 1
                k += 1
            
            col -= 1
            row += 1
            # turn down
            while row < m and flag[row][col] == 0:
                result.append(matrix[row][col])
                flag[row][col] = 1
                row += 1
                k += 1                
            
            row -= 1
            col -= 1
            # turn left
            while row >= 0 and flag[row][col] == 0:
                result.append(matrix[row][col])
                flag[row][col] = 1
                col -= 1
                k += 1

            col += 1
            row -= 1
            # turn up
            while col >= 0 and flag[row][col] == 0:
                result.append(matrix[row][col])
                flag[row][col] = 1
                row -= 1
                k += 1                                   
            
            row += 1
            col += 1
        return result
