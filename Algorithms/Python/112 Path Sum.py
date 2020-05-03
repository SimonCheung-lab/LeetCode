/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

bool findPath(struct TreeNode* node, int sum)
{
    if (node->left == NULL && node->right == NULL && sum == node->val){
        return true;
    }

    bool bfind = false;
    if (node->left){
        bfind = findPath(node->left, sum - node->val);
    }

    if (!bfind && node->right){
        bfind = findPath(node->right, sum - node->val);
    }

    return bfind;
}

bool hasPathSum(struct TreeNode* root, int sum){
    if (root == NULL){
        return false;
    }

    return findPath(root, sum);
}
