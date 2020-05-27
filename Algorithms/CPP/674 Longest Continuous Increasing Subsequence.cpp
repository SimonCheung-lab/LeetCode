class Solution {
public:
    int findLengthOfLCIS(vector<int>& nums) {
        if (nums.size() == 0) {
            return 0;
        }

        int ans, maxHere;
        ans = maxHere = 1;
        for (int i = 1; i < nums.size(); ++i) {
            if (nums[i] > nums[i - 1]) {
                maxHere += 1;
                ans = max(ans, maxHere);
            }
            else {
                maxHere = 1;
            }
        }
        return ans;
    }
};
