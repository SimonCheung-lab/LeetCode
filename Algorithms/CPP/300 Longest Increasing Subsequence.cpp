class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        if (nums.size() == 0) {
            return 0;
        }
        
        vector<int> dp(nums.size(), 1);
        for (int i = 1; i < nums.size(); ++i)
            for (int j = 0; j < i; ++j) {
                if (nums[j] < nums[i]) {
                    dp[i] = max(dp[j] + 1, dp[i]);
                }
            }
        return *std::max_element(dp.begin(), dp.end());
    }
};


class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        if (nums.size() == 0) {
            return 0;
        }

        vector<int> tail(1, nums[0]);
        for (int i = 1; i < nums.size(); ++i) {
            if (nums[i] > tail.back()) {
                tail.push_back(nums[i]);
            }
            else {
                int left, right;
                left = 0;
                right = tail.size() - 1;
                while (left < right) {
                    int mid = (left + right) / 2;
                    if (tail[mid] < nums[i]) {
                        left = mid + 1;
                    }
                    else {
                        right = mid;
                    }
                }
                // insert
                tail[left] = nums[i];
            }
        }
        return tail.size();
    }
};
