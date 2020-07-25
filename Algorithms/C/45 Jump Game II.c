// 1 greedy
int jump(int* nums, int numsSize){
    int position = numsSize - 1;
    int step = 0;
    while (position > 0) {
        for (int i = 0; i < position; ++i) {
            if (nums[i] + i >= position) {
                position = i;
                ++step;
            }
        }
    }

    return step;
}

// 2. O(n^2)
int jump(int* nums, int numsSize){
    int rightmost = 0;
    int end = 0;
    int step = 0;

    for (int i = 0; i < numsSize - 1; ++i) {
        rightmost = fmax(rightmost, nums[i] + i);
        if (i == end) {
            end = rightmost;
            ++step;
        }
    }

    return step;
}
