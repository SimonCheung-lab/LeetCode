class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.size() == 0) {
            return 0;
        }

        std::unordered_set<int> nums_set(nums.begin(), nums.end());
        int ans = 1;
        for (int i = 0; i < nums.size(); ++i) {
            if (nums_set.find(nums[i] - 1) == nums_set.end()) {
                int cur = nums[i] + 1;
                int seq_len = 1;
                while (nums_set.find(cur) != nums_set.end()) {
                    ++cur;
                    ++seq_len;
                }
                ans = max(ans, seq_len);
            }
        }
        return ans;
    }
};
