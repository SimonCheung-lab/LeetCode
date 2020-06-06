// O(n^2)
int lengthOfLIS(int* nums, int numsSize){
    if (nums == NULL || numsSize <= 0) {
        return 0;
    }

    int* dp = calloc(numsSize, sizeof(int));
    for (int i = 0; i < numsSize; ++i) {
        dp[i] = 1;
        for (int j = 0; j < i; ++j) {
            if (nums[j] < nums[i]) {
                dp[i] = fmax(dp[i], dp[j] + 1);
            }
        }
    }

    int ans = dp[0];
    for (int i = 1; i < numsSize; ++i) {
        ans = fmax(ans, dp[i]);
    }
    free(dp);
    return ans;
}
