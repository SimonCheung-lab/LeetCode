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


// O(nlogn)
int lengthOfLIS(int* nums, int numsSize){
    if (nums == NULL || numsSize <= 0) {
        return 0;
    }

    int* dp = calloc(numsSize, sizeof(int));
    dp[0] = nums[0];
    int n = 1;
    for (int i = 1; i < numsSize; ++i) {
        if (nums[i] > dp[n - 1]) {
            dp[n++] = nums[i];
        }
        else {
            int left, right;
            left = 0;
            right = n - 1;
            while (left < right) {
                int mid = left + (right - left) / 2;
                if (dp[mid] == nums[i]) {
                    break;
                }
                else if (dp[mid] < nums[i]) {
                    left = mid + 1;
                }
                else {
                    right = mid;
                }
            }
            if (left == right) {
                dp[left] = nums[i];
            }
        }
    }
    free(dp);
    return n;
}
