int minimumTotal(int** triangle, int triangleSize, int* triangleColSize){
    if (triangle == NULL || triangleSize == 0) {
        return 0;
    }

    for (int i = triangleSize - 2; i >= 0; --i) {
        for (int j = 0; j < triangleColSize[i]; ++j) {
            triangle[i][j] += fmin(triangle[i + 1][j], triangle[i + 1][j + 1]);
        }
    }

    return triangle[0][0];
}
