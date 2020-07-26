class Solution {
public:
    vector<int> grayCode(int n) {
        vector<int> ans = {0};
        int head = 1;

        for (int i = 0; i < n; ++i) {
            for (int j = ans.size() - 1; j >= 0; --j) {
                ans.push_back(head + ans[j]);
            }

            head <<= 1;
        }

        return ans;
    }
};
