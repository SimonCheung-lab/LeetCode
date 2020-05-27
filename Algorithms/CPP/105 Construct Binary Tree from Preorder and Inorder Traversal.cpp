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
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        if (preorder.size() == 0) {
            return NULL;
        }

        TreeNode* root = new TreeNode(preorder[0]);
        if (preorder.size() > 1) {
            int n = std::distance(inorder.begin(), std::find(inorder.begin(), inorder.end(), preorder[0]));
            vector<int> leftPre(preorder.begin() + 1, preorder.begin() + n + 1);
            vector<int> leftIn(inorder.begin(), inorder.begin() + n);
            vector<int> rightPre(preorder.begin() + n + 1, preorder.end());
            vector<int> rightIn(inorder.begin() + n + 1, inorder.end());
            root->left = buildTree(leftPre, leftIn);
            root->right = buildTree(rightPre, rightIn);
        }
        return root;
    }
};
