/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* searchRange(int* nums, int numsSize, int target, int* returnSize){
    int* result = (int*)malloc(sizeof(int) * 2);
    *returnSize = 2;
    result[0] = result[1] = -1;
    
    if (nums == NULL || numsSize == 0 || target < nums[0] || target > nums[numsSize - 1]){
        return result;
    }
    
    int left_target, right_target;
    left_target = right_target = -1;

    // find the left boundary of target
    int left, right;
    left = 0;
    right = numsSize - 1;
    while (left < right){
        int mid = left + (right - left) / 2;
        if (nums[mid] >= target){
            right = mid;
        }
        else{
            left = mid + 1;
        }
    }
    left_target = left;

    // find the right boundary of target
    left = 0;
    right = numsSize - 1;
    while (left < right){
        int mid = left + (right - left) / 2;
        if (nums[mid] <= target){
            left = mid + 1;
        }
        else{
            right = mid;
        }
    }
    if (nums[left] > target){
        left -= 1;
    }
    right_target = left;

    if (right_target < left_target || nums[left_target] != target){
        return result;
    }

    result[0] = left_target;
    result[1] = right_target;
    return result;       
}
