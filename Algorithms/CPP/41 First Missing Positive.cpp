class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int max_num = nums.size();
        if (max_num == 0){
            return 1;
        }

        for (int i = 1; i <= max_num; ++i){
            if (std::find(nums.begin(), nums.end(), i) == nums.end()){
                return i;
            }
        }

        return max_num + 1;
    }
};
