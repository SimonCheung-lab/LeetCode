class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<vector<bool>> rows(9, vector<bool>(10, false));
        vector<vector<bool>> columns(9, vector<bool>(10, false));
        vector<vector<bool>> subboxes(9, vector<bool>(10, false));

        int n, boxIndex;
        for (int i = 0; i < 9; ++i) {
            for (int j = 0; j < 9; ++j) {
                if (board[i][j] != '.') {
                    n = board[i][j] - '0';
                    boxIndex =  (i / 3) * 3 + j / 3;
                    if (rows[i][n] || columns[j][n] || subboxes[boxIndex][n]) {
                        return false;
                    }
                    else {
                        rows[i][n] = true;
                        columns[j][n] = true;
                        subboxes[boxIndex][n] = true;
                    }
                }
            }
        }

        return true;
    }
};
