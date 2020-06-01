class Solution {
public:
    vector<string> generateParenthesis(int n) {
        this->n = n;
        backtrack(0, 0);
        return ans;
    }

    void backtrack(int left, int right) {
        if (left == n && right == n) {
            ans.push_back(parentheses);
            return;
        }

        if (left < n) {
            parentheses.push_back('(');
            backtrack(left + 1, right);
            parentheses.erase(parentheses.size() - 1);
        }

        if (right < left) {
            parentheses.push_back(')');
            backtrack(left, right + 1);
            parentheses.erase(parentheses.size() - 1);
        }
    }

private:
    string parentheses;
    vector<string> ans;
    int n;
};
