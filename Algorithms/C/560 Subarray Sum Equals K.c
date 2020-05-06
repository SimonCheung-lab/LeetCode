int subarraySum(int* nums, int numsSize, int k){
    if (nums == NULL || numsSize == 0){
        return 0;
    }

    int result = 0;
    int* s = (int*)malloc(sizeof(int) * numsSize);
    memset(s, 0, sizeof(int) * numsSize);
    s[0] = nums[0];
    if (s[0] == k){
        ++result;
    }
    for (int i = 1; i < numsSize; ++i){
        s[i] = s[i - 1] + nums[i];
        if (s[i] == k){
            ++result;
        }
    }

    for (int i = 1; i < numsSize; ++i)
        for (int j = i; j < numsSize; ++j){
            if (j == i){
                s[j] = nums[j];
            }
            else{
                s[j] = s[j] - s[i - 1];
            }
            if (s[j] == k){
                ++result;
            }
        }

    free(s);
    return result;
}
