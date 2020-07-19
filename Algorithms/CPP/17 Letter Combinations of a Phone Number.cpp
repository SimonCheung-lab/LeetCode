class Solution {
public:
    vector<string> letterCombinations(string digits) {
        if (digits.size() == 0) {
            return vector<string>();    
        }

        tmp = string(digits.size(), 'a');
        this->digits = digits;
        backtracking(0);
        
        return ans;
    }

    void backtracking(int i) {
        if (i == digits.size()) {
            ans.push_back(tmp);
            return;
        }

        for (const auto& alpha : number_to_alpha[digits[i]]) {
            tmp[i] = alpha;
            backtracking(i + 1);
        }
    }

    Solution() {
        number_to_alpha['2'] = "abc";
        number_to_alpha['3'] = "def";
        number_to_alpha['4'] = "ghi";
        number_to_alpha['5'] = "jkl";
        number_to_alpha['6'] = "mno";
        number_to_alpha['7'] = "pqrs";
        number_to_alpha['8'] = "tuv";
        number_to_alpha['9'] = "wxyz";
    }

private:
    map<char, string> number_to_alpha;
    string digits;
    string tmp;
    vector<string> ans;
};
