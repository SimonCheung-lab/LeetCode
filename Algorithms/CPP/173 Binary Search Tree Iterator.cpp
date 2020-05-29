/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class BSTIterator {
public:
    BSTIterator(TreeNode* root) {
        inorder(root);
    }
    
    /** @return the next smallest number */
    int next() {
        int ans = data.front();
        data.pop();
        return ans;
    }
    
    /** @return whether we have a next smallest number */
    bool hasNext() {
        return !data.empty();
    }

    void inorder(TreeNode* root) {
        if (root == NULL) {
            return;
        }

        inorder(root->left);
        data.push(root->val);
        inorder(root->right);
    }

private:
    std::queue<int> data;
};

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator* obj = new BSTIterator(root);
 * int param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */


// solution 2
class BSTIterator {
public:
    BSTIterator(TreeNode* root) {
        leftMost(root);
    }
    
    /** @return the next smallest number */
    int next() {
        TreeNode* node = stack.top();
        stack.pop();
        leftMost(node->right);
        return node->val;
    }
    
    /** @return whether we have a next smallest number */
    bool hasNext() {
        return !stack.empty();
    }

    void leftMost(TreeNode* node) {
        while (node) {
            stack.push(node);
            node = node->left;
        }
    }

private:
    std::stack<TreeNode*> stack;
};
