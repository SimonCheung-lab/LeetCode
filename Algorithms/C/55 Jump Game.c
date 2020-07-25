bool canJump(int* nums, int numsSize){
    int rightmost = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (i <= rightmost) {
            rightmost = fmax(rightmost, i + nums[i]);
        }
    }

    return rightmost >= numsSize - 1;
}
