// 分割算法 O(n)
class Solution {
public:
    string kthLargestNumber(vector<string>& nums, int k) {
        std::nth_element(nums.begin(), nums.begin() + k - 1, nums.end(), [](const std::string& a, const std::string& b){
            return a.size() == b.size() ? a > b : a.size() > b.size();
        });
        return nums[k - 1];
    }
};
