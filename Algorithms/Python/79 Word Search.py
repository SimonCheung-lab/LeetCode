class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def find(i, j, t, path):
            if t == n:
                return True
            
            adjacent = []
            if j > 0:
                adjacent.append((i, j -1))
            if i > 0:
                adjacent.append((i - 1, j))
            if j < column - 1:
                adjacent.append((i, j + 1))
            if i < row - 1:
                adjacent.append((i + 1, j))

            for cor in adjacent:
                if cor not in path:
                    if board[cor[0]][cor[1]] == word[t]:
                        path.append(cor)
                        if find(cor[0], cor[1], t + 1, path[:]):
                            return True
                        path.pop()  

            return False         

        def search(i):
            if word[0] not in board[i]:
                return False
            
            count = board[i].count(word[0])
            j = 0
            while count:
                j = board[i][j:].index(word[0]) + j
                path = []
                path.append((i, j))
                if find(i, j, 1, path):
                    return True
                j += 1
                count -= 1

            return False

        def backtrack(i=0):
            if i == row:
                return False
            
            if search(i):
                return True
            
            return backtrack(i + 1)

        row, column = len(board), len(board[0])
        n = len(word)
        if n == 0:
            return False
        return backtrack()
