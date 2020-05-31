class Solution {
public:
    vector<vector<int>> combinationSum3(int k, int n) {
        this->k = k;
        dfs(1, n);
        return ans;
    }

    void dfs(int start, int target) {
        if (path.size() == k && target == 0) {
            ans.push_back(path);
            return;
        }

        if (path.size() < k && target > 0) {
            for (int i = start; i < 10; ++i) {
                path.push_back(i);
                dfs(i + 1, target - i);
                path.pop_back();
            }
        }
    }

private:
    vector<vector<int>> ans;
    vector<int> path;
    int k;
};
