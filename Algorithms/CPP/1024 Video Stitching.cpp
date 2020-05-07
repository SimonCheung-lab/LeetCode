class Solution {
public:
    int videoStitching(vector<vector<int>>& clips, int T) {
        // important
        sort(clips.begin(), clips.end(), [](vector<int>& c1, vector<int>& c2){
            return c1[0] < c2[0] || (c1[0] == c2[0] && c1[1] < c2[1]);
        });

        // dp[i] is the minimal clips to cover [0, i]
        vector<int> dp(T + 1, -1);
        for (auto c : clips){
            if (c[0] > T){
                continue;
            }

            if (c[0] == 0){
                for (int i = 0; i <= min(c[1], T); ++i){
                    dp[i] = 1;
                }
                continue;
            }

            if (dp[c[0]] == -1){
                // just break
                break;
            }

            int m = dp[c[0]];
            for (int i = c[0] + 1; i <= min(c[1], T); ++i){
                if (dp[i] > 0){
                    m = min(m, dp[i]);
                }
                else{
                    dp[i] = m + 1;
                }
            }
        }
        return dp[T];
    }
};
