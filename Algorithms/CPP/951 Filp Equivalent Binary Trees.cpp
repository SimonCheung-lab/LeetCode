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
    bool flipEquiv(TreeNode* root1, TreeNode* root2) {
        flip(root1);
        flip(root2);

        return equal(root1, root2);
    }

    bool equal(TreeNode* root1, TreeNode* root2) {
        if (root1 == NULL && root2 == NULL) {
            return true;
        }

        if (root1 && root2 && root1->val == root2->val) {
            return equal(root1->left, root2->left) && equal(root1->right, root2->right);
        }

        return false;
    }

    void flip(TreeNode* root) {
        if (root == NULL) {
            return;
        }

        if (root->right == NULL || (root->left && root->left->val > root->right->val)) {
            // swap
            TreeNode* node = root->left;
            root->left = root->right;
            root->right = node;
        }

        flip(root->left);
        flip(root->right);
    }
};
