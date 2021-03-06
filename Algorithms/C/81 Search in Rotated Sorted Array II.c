bool search(int* nums, int numsSize, int target){
    int left, right, mid;
    left = 0;
    right = numsSize - 1;

    while (left <= right) {
        mid = (left + right) / 2;

        if (nums[mid] == target) {
            return true;
        }

        if (nums[left] == nums[mid]) {
            left++;
            continue;
        }

        if (nums[right] == nums[mid]) {
            right--;
            continue;
        }

        if (nums[left] < nums[mid]) {
            if (nums[left] <= target && target < nums[mid]) {
                right = mid - 1;
            }
            else {
                left = mid + 1;
            }
        }
        else {
            if (nums[mid] < target && target <= nums[right]) {
                left = mid + 1;
            }
            else {
                right = mid - 1;
            }
        }
    }

    return false;
}
