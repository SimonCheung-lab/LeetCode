class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(), [](vector<int>& x, vector<int>& y){
            return x[0] < y[0];
        });

        vector<vector<int>> result;
        for (auto i: intervals){
            if (result.empty()){
                result.push_back(i);
            }
            else{
                auto v = result.back();
                if (i[0] <= v[1]){
                    // merge
                    vector<int> merge_v = {v[0], max(v[1], i[1])};
                    result.pop_back();
                    result.push_back(merge_v);
                }
                else{
                    result.push_back(i);
                }
            }
        }
        return result;
    }
};
