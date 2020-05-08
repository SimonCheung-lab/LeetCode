int uniquePaths(int m, int n){
    int* dp = (int*)malloc(sizeof(int)*n);
    for (int i = 0; i < n; ++i){
        dp[i] = 1;
    }
    for (int i = 1; i < m; ++i)
        for (int j = 0; j < n; ++j){
            if (j == 0){
                dp[j] = 1;
            }
            else{
                dp[j] = dp[j] + dp[j - 1];
            }
        }
    int result = dp[n - 1];
    free(dp);
    return result;
}
