/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<TreeNode*> findDuplicateSubtrees(TreeNode* root) {
        serialize(root);
        return ans;
    }

    string serialize(TreeNode* node) {
        if (node == NULL) {
            return "#";
        }

        string key = to_string(node->val) + "," + serialize(node->left) + "," + serialize(node->right);

        if (++cache[key] == 2) {
            ans.push_back(node);
        }

        return key;
    }

private:
    vector<TreeNode*> ans;
    unordered_map<string, int> cache;
};
