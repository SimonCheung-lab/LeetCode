class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [{} for _ in range(9)]
        columns = [{} for _ in range(9)]
        subboxes = [{} for _ in range(9)]

        for i in range(9):
            for j in range(9):
                n = board[i][j]
                if n != '.':
                    n = int(n)
                    rows[i][n] = rows[i].get(n, 0) + 1
                    columns[j][n] = columns[j].get(n, 0) + 1
                    box_index = (i // 3) * 3 + j // 3
                    subboxes[box_index][n] = subboxes[box_index].get(n, 0) + 1

                    if rows[i][n] > 1 or columns[j][n] > 1 or subboxes[box_index][n] > 1:
                        return False
        
        return True
