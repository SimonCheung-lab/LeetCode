class Solution {
public:
    int longestValidParentheses(string s) {
        s = "#" + s + "#";
        int ans = 0;
        std::vector<pair<int, char>> v;
        for (int i = 0; i < s.size(); ++i) {
            if (s[i] == ')' && !v.empty() && v.back().second == '(') {
                v.pop_back();
                ans = max(ans, i - v.back().first);
            }
            else {
                v.push_back(make_pair(i, s[i]));
            }
        }

        // int ans = 0;
        // for (int i = 1; i < v.size(); ++i) {
        //     ans = max(ans, v[i].first - v[i - 1].first - 1);
        // }

        return ans;
    }
};


// solution 2, more faster
class Solution {
public:
    int longestValidParentheses(string s) {
        s = "#" + s + "#";
        std::vector<int> v;
        for (int i = 0; i < s.size(); ++i) {
            if (s[i] == ')' && !v.empty() && s[v.back()] == '(') {
                v.pop_back();
            }
            else {
                v.push_back(i);
            }
        }

        int ans = 0;
        for (int i = 1; i < v.size(); ++i) {
            ans = max(ans, v[i] - v[i - 1] - 1);
        }

        return ans;
    }
};


// solution 3, space cost O(1)
class Solution {
public:
    int longestValidParentheses(string s) {
        int ans = 0;
        int left, right;
        left = right = 0;
        // from left to right
        for (int i = 0; i < s.size(); ++i) {
            if (s[i] == '(') {
                ++left;
            }
            else if (s[i] == ')') {
                ++right;
                if (right == left) {
                    ans = max(ans, left + right);
                }
                else if (right > left) {
                    left = right = 0;
                }
            }
        }

        left = right = 0;
        // from right to left
        for (int i = s.size() - 1; i >= 0; --i) {
            if (s[i] == ')') {
                ++right;
            }
            else if (s[i] == '(') {
                ++left;
                if (left == right) {
                    ans = max(ans, left + right);
                }
                else if (left > right) {
                    left = right = 0;
                }
            }
        }

        return ans;
    }
};
