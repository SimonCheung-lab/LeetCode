/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

struct TreeNode* pre_node = NULL;
bool valid = true;

void inorder(struct TreeNode* node) {
    if (node == NULL) {
        return;
    }

    inorder(node->left);

    if (pre_node == NULL || pre_node->val >= node->val) {
        pre_node = node;
    }
    else {
        valid = false;
        return;
    }

    inorder(node->right);
}

bool isValidBST(struct TreeNode* root){
    valid = true;
    inorder(root);
    return valid;
}
