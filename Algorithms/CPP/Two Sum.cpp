class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
	    unordered_map<int, int> map;
	    vector<int> result;
	    for (int i = 0; i < nums.size(); ++i) {
		    if (map.find(target - nums[i]) != map.end()) {
			    result.push_back(i);
			    result.push_back(map[target - nums[i]]);
          # assume only one solution
          break;
		    }
		    else {
			    map[nums[i]] = i;
		    }
	    }

	    return result;
    }
};
