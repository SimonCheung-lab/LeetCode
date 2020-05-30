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
    vector<TreeNode*> allPossibleFBT(int N) {
        if (N % 2 == 0) {
            return vector<TreeNode*>();
        }

        return buildFBT(N);
    }

    vector<TreeNode*> buildFBT(int n) {
        vector<TreeNode*> ans;
        if (n == 1) {
            ans.push_back(new TreeNode(0));
            return ans;
        }

        for (int i = 1; i < n - 1; i += 2) {
            vector<TreeNode*> l = buildFBT(i);
            vector<TreeNode*> r = buildFBT(n - 1 - i);
            for (auto left : l)
                for (auto right : r) {
                    TreeNode* root = new TreeNode(0);
                    root->left = left;
                    root->right = right;
                    ans.push_back(root);
                }
        }

        return ans;
    }
};
