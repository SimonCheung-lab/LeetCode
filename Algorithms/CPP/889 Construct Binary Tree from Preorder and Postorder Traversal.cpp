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
    TreeNode* constructFromPrePost(vector<int>& pre, vector<int>& post) {
        if (pre.size() == 0) {
            return NULL;
        }

        TreeNode* root = new TreeNode(pre[0]);
        if (pre.size() > 1) {
            int n = std::distance(post.begin(), std::find(post.begin(), post.end(), pre[1])) + 1;
            vector<int> leftPre(pre.begin() + 1, pre.begin() + n + 1);
            vector<int> leftPost(post.begin(), post.begin() + n);
            vector<int> rightPre(pre.begin() + n + 1, pre.end());
            vector<int> rightPost(post.begin() + n, post.end() - 1);
            root->left = constructFromPrePost(leftPre, leftPost);
            root->right = constructFromPrePost(rightPre, rightPost);
        }
        return root;
    }
};
