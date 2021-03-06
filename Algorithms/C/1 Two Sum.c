int find(int* nums, int numSize, int target)
{
    if (numSize < 1){
        return -1;
    }

    if(nums[numSize - 1] == target){
        return numSize - 1;
    }

    int tmp = nums[numSize - 1];
    nums[numSize - 1] = target;

    int i = 0;
    while (nums[i] != target){
        ++i;
    }
    nums[numSize - 1] = tmp;

    if (i == numSize - 1){
        return -1;
    }

    return i;
}

int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    int* result = (int*)malloc(sizeof(int)*2);
    *returnSize = 2;
    int *m = (int*)malloc(sizeof(int)*numsSize);
    int len_m = 0;
    for (int i = 0; i < numsSize; ++i){
        int find_i = find(m, len_m, target - nums[i]);
        if (find_i != -1){
            result[0] = i;
            result[1] = find_i;
            // assume only one solution
            break; 
        }
        else{
            m[len_m] = nums[i];
            ++len_m;
        }
    }

    free(m);
    return result;
}
