class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        std::sort(candidates.begin(), candidates.end());
        this->candidates = candidates;
        dfs(0, target);
        return ans;
    }

    void dfs(int start, int target) {
        if (target == 0) {
            ans.push_back(path);
            return;
        }
        
        for (int i = start; i < candidates.size() && target - candidates[i] >= 0; ++i) {
            path.push_back(candidates[i]);
            dfs(i, target - candidates[i]);
            path.pop_back();
        }
    }

private:
    vector<int> path;
    vector<int> candidates;
    vector<vector<int>> ans;
};
