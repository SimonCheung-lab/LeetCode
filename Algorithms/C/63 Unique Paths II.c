int uniquePathsWithObstacles(int** obstacleGrid, int obstacleGridSize, int* obstacleGridColSize){
    int* dp = (int*)malloc(sizeof(int)*(*obstacleGridColSize));
    for (int i = 0; i < *obstacleGridColSize; ++i){
        if (obstacleGrid[0][i] == 1 || (i > 0 && dp[i - 1] == 0)){
            dp[i] = 0;
        }
        else{
            dp[i] = 1;
        }
    }

    for (int i = 1; i < obstacleGridSize; ++i)
        for (int j = 0; j < *obstacleGridColSize; ++j){
            if (obstacleGrid[i][j] == 1 || (j == 0 && dp[j] == 0)){
                dp[j] = 0;
            }
            else{
                if (j == 0){
                    dp[j] = 1;
                }
                else{
                    dp[j] = dp[j] + dp[j - 1];
                }
            }
        }

    int result = dp[*obstacleGridColSize - 1];
    free(dp);
    return result;
}
