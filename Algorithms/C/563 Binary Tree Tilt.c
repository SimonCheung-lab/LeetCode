/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

// not a smart solution
int sum_of_subtree(struct TreeNode* node)
{
    int s = 0;
    if (node->left) {
        s = node->left->val + sum_of_subtree(node->left);
    }
    if (node->right) {
        s += node->right->val + sum_of_subtree(node->right);
    }

    return s;
}

int findTilt(struct TreeNode* root){
    if (root == NULL){
        return 0;
    }

    int tilt = 0;
    int left_sum = 0;
    if (root->left){
        left_sum = sum_of_subtree(root->left) + root->left->val;
    }
    int right_sum = 0;
    if (root->right){
        right_sum = sum_of_subtree(root->right) + root->right->val;
    }
    tilt = abs(left_sum - right_sum);

    return tilt + findTilt(root->left) + findTilt(root->right);
}
