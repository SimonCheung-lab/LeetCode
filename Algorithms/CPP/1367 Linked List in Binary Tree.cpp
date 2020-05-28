/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
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
    bool isSubPath(ListNode* head, TreeNode* root) {
        if (head == NULL || root == NULL) {
            return false;
        }

        return explorePath(head, root) || isSubPath(head, root->left) || isSubPath(head, root->right);
    }

    bool explorePath(ListNode* node, TreeNode* treeNode) {
        if (node == NULL) {
            return true;
        }

        if (treeNode == NULL) {
            return false;
        }

        if (treeNode->val != node->val) {
            return false;
        }
        
        return explorePath(node->next, treeNode->left) || explorePath(node->next, treeNode->right);
    }
};
