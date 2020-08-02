/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

// 1
bool helper(struct TreeNode* root, struct TreeNode* min_node, struct TreeNode* max_node) {
    if (root == NULL) {
        return true;
    }

    if (min_node && root->val <= min_node->val) {
        return false;
    }    

    if (max_node && root->val >= max_node->val) {
        return false;
    }

    return helper(root->left, min_node, root) && helper(root->right, root, max_node);
}

bool isValidBST(struct TreeNode* root){
    return helper(root, NULL, NULL);
}


// 2
struct TreeNode* preNode = NULL;

bool inorder(struct TreeNode* node) {
    if (node == NULL) {
        return true;
    }

    if (!inorder(node->left)) {
        return false;
    }

    if (preNode && preNode->val >= node->val) {
        return false;
    }

    preNode = node;

    return inorder(node->right);
}

bool isValidBST(struct TreeNode* root){
    return inorder(root);
}
