/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

void add_one_row_at(struct TreeNode* node, int D, int v, int d)
{
    if (D + 1 == d){
        struct TreeNode* pLeft = node->left;
        struct TreeNode* pRight = node->right;
        struct TreeNode* newLeft = (struct TreeNode*)malloc(sizeof(struct TreeNode));
        struct TreeNode* newRight = (struct TreeNode*)malloc(sizeof(struct TreeNode));
        newLeft->val = v;
        newLeft->left = pLeft;
        newLeft->right = NULL;
        newRight->val = v;
        newRight->left = NULL;
        newRight->right = pRight;
        node->left = newLeft;
        node->right = newRight;
        return;
    }

    if (node->left){
        add_one_row_at(node->left, D + 1, v, d);
    }

    if (node->right){
        add_one_row_at(node->right, D + 1, v, d);
    }
}

struct TreeNode* addOneRow(struct TreeNode* root, int v, int d){
    if (d == 1){
        struct TreeNode* node = (struct TreeNode*)malloc(sizeof(struct TreeNode));
        node->val = v;
        node->left = root;
        node->right = NULL;
        return node;
    }

    add_one_row_at(root, 1, v, d);
    return root;
}
