class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> ans;
        do_permute(nums, 0, nums.size() - 1, ans);
        return ans;
    }

    void do_permute(vector<int>& nums, int from, int to, vector<vector<int>>& ans) {
        if (from == to) {
            // print(nums);
            // ans.push_back(vector<int>(nums.begin(), nums.end()));  // 1
            // ans.emplace_back(nums);  // same with 1
            ans.push_back(nums);  // faster than emplace_back
            return;
        }

        for (int i = from; i <= to; ++i) {
            swap(nums[from], nums[i]);
            do_permute(nums, from + 1, to, ans);
            swap(nums[i], nums[from]);
        }
    }

    void print(vector<int>& nums) {
        for (int i = 0; i < nums.size(); ++i) {
            std::cout << nums[i];
        }
        std::cout << std::endl;
    }
};
