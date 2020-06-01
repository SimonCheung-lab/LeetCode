class Solution {
public:
    bool isValid(string s) {
        std::stack<char> parentheses;
        for (auto c : s) {
            if (c == ')' || c == ']' || c == '}') {
                if (parentheses.empty()) {
                    return false;
                }
                if ((c == ')' && parentheses.top() == '(') 
                || (c == ']' && parentheses.top() == '[')
                || (c == '}' && parentheses.top() == '{')) {
                    parentheses.pop();
                }
                else {
                    return false;
                }
            }
            else {
                parentheses.push(c);
            }
        }

        return parentheses.empty();
    }
};
