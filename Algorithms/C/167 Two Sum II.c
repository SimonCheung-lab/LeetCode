/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* numbers, int numbersSize, int target, int* returnSize){
    int* result = (int*)malloc(sizeof(int) * 2);
    result[0] = result[1] = 1;
    *returnSize = 2;
    int left, right;
    left = 0;
    right = numbersSize - 1;
    while (left < right){
        int s = numbers[left] + numbers[right];
        if (s == target){
            break;
        }
        else if (s < target){
            ++left;
        }
        else{
            --right;
        }
    }
    result[0] = left + 1;
    result[1] = right + 1;
    return result;
}
