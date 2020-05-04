int result;
int N;
int* queen_position;

bool is_ok(int row, int column)
{
    if (row == 0){
        return true;
    }

    int left_up, right_up;
    left_up = column - 1;
    right_up = column + 1;
    for (int r = row - 1; r >= 0; --r){
        if (queen_position[r] == column){
            return false;
        }
        if (left_up >= 0 && queen_position[r] == left_up){
            return false;
        }
        if (right_up < N && queen_position[r] == right_up){
            return false;
        }
        --left_up;
        ++right_up;
    }

    return true;
}

void n_queen(int row)
{
    if (row == N){
        ++result;
        return;
    }

    for (int c = 0; c < N; ++c){
        if (is_ok(row, c)){
            queen_position[row] = c;
            n_queen(row + 1);
        }
    }
}

int totalNQueens(int n){
    N = n;
    result = 0;
    queen_position = (int*)malloc(sizeof(int)*n);
    memset(queen_position, 0, sizeof(int)*n);
    n_queen(0);
    free(queen_position);
    queen_position = NULL;
    return result;
}
