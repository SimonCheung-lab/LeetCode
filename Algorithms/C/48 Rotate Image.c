void swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

void rotate(int** matrix, int matrixSize, int* matrixColSize){
    if (matrix == NULL || matrixSize <= 1) {
        return;
    }

    // transpose
    for (int i = 0; i < matrixSize; ++i)
        for (int j = 0; j < i; ++j) {
            swap(&matrix[i][j], &matrix[j][i]);
        }

    // reverse each row
    for (int i = 0; i < matrixSize; ++i) {
        for (int start = 0, end = matrixSize - 1; start < end; ++start, --end) {
            swap(&matrix[i][start], &matrix[i][end]);
        }
    }
}
