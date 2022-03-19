class Solution {
public:
    vector<int> findPeakGrid(vector<vector<int>>& mat) {
        int left = 0, right = mat[0].size() - 1;
        while (left <= right)
        {
            int column = (left + right) / 2;
            int max_row = findMaxRow(mat, column);
            if (isPeak(mat, max_row, column))
            {
                return vector<int>{max_row, column};
            }
            mat[max_row][column + 1] > mat[max_row][column] ? left = column + 1 : right = column - 1;
        }
        return vector<int>{0, 0};
    }

private:
    int findMaxRow(vector<vector<int>>& mat, int column)
    {
        int max_row = 0;
        for (int row = 1; row < mat.size(); row++)
        {
            if (mat[row][column] > mat[max_row][column])
            {
                max_row = row;
            }
        }
        return max_row;
    }

    bool isPeak(vector<vector<int>>& mat, int row, int column)
    {
        if (row == 0)
        {
            if (column == 0)
            {
                return mat[row][column] > mat[row + 1][column] && mat[row][column] > mat[row][column + 1];
            }
            if (column == mat[0].size() - 1)
            {
                return mat[row][column] > mat[row + 1][column] && mat[row][column] > mat[row][column - 1];
            }
            return mat[row][column] > mat[row + 1][column] && mat[row][column] > mat[row][column - 1] && mat[row][column] > mat[row][column + 1];
        }

        if (row == mat.size() - 1)
        {
            if (column == 0)
            {
                return mat[row][column] > mat[row - 1][column] && mat[row][column] > mat[row][column + 1];
            }
            if (column == mat[0].size() - 1)
            {
                return mat[row][column] > mat[row - 1][column] && mat[row][column] > mat[row][column - 1];
            }
            return mat[row][column] > mat[row - 1][column] && mat[row][column] > mat[row][column - 1] && mat[row][column] > mat[row][column + 1];
        }

        return mat[row][column] > mat[row][column - 1] && mat[row][column] > mat[row - 1][column]
                && mat[row][column] > mat[row][column + 1] && mat[row][column] > mat[row + 1][column];
    }
};
