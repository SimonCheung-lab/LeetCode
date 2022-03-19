class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        std::qsort(nums.data(), nums.size(), sizeof(int), [](const void* x, const void* y){
            return *(const int*)x - *(const int*)y;
        });
        return nums;
    }
};
