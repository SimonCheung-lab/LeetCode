// O(n^2)
class Solution {
public:
    int countSubstrings(string s) {
        int ans = s.size();
        vector<vector<bool>> dp(s.size(), vector<bool>(s.size(), false));
        for (int i = 1; i < s.size(); ++i) {
            for (int j = 0; j < i; ++j) {
                if (s[j] == s[i]) {
                    if (i - j < 3) {
                        dp[j][i] = true;
                    }
                    else {
                        dp[j][i] = dp[j + 1][i - 1];
                    }
                }

                if (dp[j][i]) {
                    ++ans;
                }
            }
        }
        return ans;
    }
};
