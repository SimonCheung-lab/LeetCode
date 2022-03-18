bool compare(char* a, char* b)
{
    if (strlen(a) == strlen(b))
    {
        return strcmp(a, b) > 0;
    }

    return strlen(a) > strlen(b);
}

void swap(char** a, char** b)
{
    char* c = *a;
    *a = *b;
    *b = c;
}

// 分割算法 O(n) 
int partition(char** nums, int left, int right)
{
    char* pivot = nums[right];
    int i = left;
    for (int j = i; j < right; j++)
    {
        if (compare(nums[j], pivot))
        {
            swap(&nums[i], &nums[j]);
            i++;
        }
    }
    swap(&nums[i], &nums[right]);
    return i;
}

char * kthLargestNumber(char ** nums, int numsSize, int k){
    int i = partition(nums, 0, numsSize - 1);
    if (i + 1 == k)
    {
        return nums[i];
    }

    if (i + 1 > k)
    {
        return kthLargestNumber(nums, i, k);
    }

    return kthLargestNumber(nums + (i + 1), numsSize - (i + 1), k - (i + 1));
}
