bool checkSubarraySum(int* nums, int numsSize, int k){
    if (nums == NULL || numsSize == 0){
        return false;
    }

    int* s = (int*)malloc(sizeof(int) * numsSize);
    memset(s, 0, sizeof(int) * numsSize);
    s[0] = nums[0];

    for (int i = 1; i < numsSize; ++i){
        int m = s[i - 1] + nums[i];
        if (k == 0){
            if (m == 0){
                free(s);
                return true;
            }
        }
        else if (m % k == 0){
            free(s);
            return true;
        }
        s[i] = m;
    }
    
    for (int i = 1; i < numsSize; ++i)
        for (int j = i; j < numsSize; ++j){
            if (j == i){
                s[j] = nums[i];
            }
            else{
                s[j] = s[j] - s[i - 1];
                if (k == 0){
                    if (s[j] == 0){
                        free(s);
                        return true;
                    }
                }
                else if (s[j] % k == 0){
                    free(s);
                    return true;
                }        
            }
        }

    free(s);
    return false;
}
