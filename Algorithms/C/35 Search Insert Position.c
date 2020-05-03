int searchInsert(int* nums, int numsSize, int target){
    if (nums == NULL || numsSize == 0 || target <= nums[0]){
        return 0;
    }

    if (target > nums[numsSize - 1]){
        return numsSize;
    }

    int left, right;
    left = 0;
    right = numsSize - 1;
    while (left < right){
        int mid = (left + right) / 2;
        if (nums[mid] == target){
            return mid;
        }
        else if (nums[mid] > target){
            right = mid;
        }
        else{
            left = mid + 1;   
        }
    }

    return left;
}
