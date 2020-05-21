class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        if (triangle.size() == 0){
            return 0;
        }

        vector<int> dp(triangle.size(), 0);
        dp[0] = triangle[0][0];
        for (int i = 1; i < triangle.size(); ++i){
            vector<int> tmp = dp;
            for (int j = 0; j < i + 1; ++j){
                if (j == 0){
                    dp[j] = tmp[0] + triangle[i][0];
                }
                else if (j == i){
                    dp[j] = tmp[j - 1] + triangle[i][j];
                }
                else {
                    dp[j] = min(tmp[j - 1], tmp[j]) + triangle[i][j];
                }
            }
        }

        return *std::min_element(dp.begin(), dp.end());
    }
};
