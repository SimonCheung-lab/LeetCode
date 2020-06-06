class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        bool rows[9][10] = {false};
        bool columns[9][10] = {false};
        bool subboxes[9][10] = {false};

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
