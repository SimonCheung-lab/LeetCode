class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        vector<bool> has(nums.size() + 1, false);
        for (int i = 0; i < nums.size(); ++i) {
            has[nums[i]] = true;
        }

        vector<int> ans;
        for (int i = 1; i < has.size(); ++i) {
            if (has[i] == false) {
                ans.push_back(i);
            }
        }
        return ans;
    }
};
