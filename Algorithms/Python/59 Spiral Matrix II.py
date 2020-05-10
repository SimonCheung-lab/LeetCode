class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0] * n for _ in range(n)]
        k = 1
        row, col = 0, 0
        while k <= n ** 2:
            # turn right
            while col < n and result[row][col] == 0:
                result[row][col] = k
                k += 1
                col += 1

            # turn down
            row += 1
            col -= 1
            while row < n and result[row][col] == 0:
                result[row][col] = k
                k += 1
                row += 1

            # turn left
            row -= 1
            col -= 1
            while col >= 0 and result[row][col] == 0:
                result[row][col] = k
                k += 1
                col -= 1

            # turn up
            row -= 1
            col += 1
            while row >= 0 and result[row][col] == 0:
                result[row][col] = k
                k += 1
                row -= 1

            row += 1
            col += 1

        return result
