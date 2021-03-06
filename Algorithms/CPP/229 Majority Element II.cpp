class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        if (nums.size() < 2) {
            return nums;
        }

        int n = nums.size();

        int candidate1, candidate2;
        candidate1 = candidate2 = nums[0];
        int count1, count2;
        count1 = count2 = 0;

        for (auto num : nums) {
            if (num == candidate1) {
                count1++;
                continue;
            }

            if (num == candidate2) {
                count2++;
                continue;
            }

            if (count1 == 0) {
                candidate1 = num;
                count1 = 1;
                continue;
            }

            if (count2 == 0) {
                candidate2 = num;
                count2 = 1;
                continue;
            }

            count1--;
            count2--;
        }

        count1 = count2 = 0;
        for (auto num : nums) {
            if (num == candidate1) {
                count1++;
            }
            else if (num == candidate2) {
                count2++;
            }
        }

        vector<int> ans;
        if (count1 > n / 3) {
            ans.push_back(candidate1);
        }

        if (count2 > n / 3) {
            ans.push_back(candidate2);
        }

        return ans;
    }
};
