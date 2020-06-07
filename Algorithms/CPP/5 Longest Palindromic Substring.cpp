// O(n^2)
class Solution {
public:
    string longestPalindrome(string s) {
        vector<vector<bool>> dp(s.size(), vector<bool>(s.size(), false));
        int start, max_len;
        start = 0;
        max_len = 1;
        for (int i = 1; i < s.size(); ++i){
            for (int j = 0; j < s.size(); ++j) {
                if (s[j] == s[i]) {
                    if (i - j < 3) {
                        dp[j][i] = true;
                    }
                    else {
                        dp[j][i] = dp[j + 1][i - 1];
                    }
                }

                if (dp[j][i] && i - j + 1 > max_len) {
                    start = j;
                    max_len = i - j + 1;
                }
            }
        }
        return string(s.begin() + start, s.begin() + start + max_len);
    }
};
