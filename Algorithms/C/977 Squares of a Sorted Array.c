/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* sortedSquares(int* A, int ASize, int* returnSize){
    int* result = (int*)malloc(sizeof(int) * ASize);
    memset(result, 0, sizeof(int) * ASize);
    *returnSize = ASize;
    int i, j, k;
    i = 0, j = ASize - 1, k = ASize - 1;
    while (i <= j){
        if (abs(A[i]) >= abs(A[j])){
            result[k] = pow(A[i], 2);
            ++i;
        }
        else{
            result[k] = pow(A[j], 2);
            --j;
        }
        --k;
    }
    return result;
}
