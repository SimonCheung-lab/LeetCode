/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    string tree2str(TreeNode* t) {
        return preorder(t);
    }

    string preorder(TreeNode* node) {
        if (node == NULL) {
            return "";
        }

        string left = preorder(node->left);
        string right = preorder(node->right);
        string ans = to_string(node->val);

        if (!right.empty()) {
            ans += "(" + left + ")" + "(" + right + ")";
        }
        else if (!left.empty()) {
            ans += "(" + left + ")";
        }

        return ans;
    }
};
