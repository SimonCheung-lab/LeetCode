int compare (const void * a, const void * b){
  return ( *(int*)a - *(int*)b );
}

int threeSumClosest(int* nums, int numsSize, int target){
    int ans = nums[0] + nums[1] + nums[2];
    qsort(nums, numsSize, sizeof(int), compare);
    int s;
    for (int i = 0; i < numsSize - 2; ++i) {
        int j, k;
        j = i + 1, k = numsSize - 1;
        while (j < k) {
            s = nums[i] + nums[j] + nums[k];
            if (abs(s - target) < abs(ans - target)) {
                ans = s;
            }
            if (s == target) {
                return target;
            }
            else if (s < target) {
                ++j;
            }
            else {
                --k;
            }
        }
    }
    return ans;
}
