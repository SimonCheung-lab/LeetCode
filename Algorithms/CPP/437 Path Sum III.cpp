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
    int pathSum(TreeNode* root, int sum) {
        this->sum = sum;
        result = 0;
        cache = {{0,1}};
        dfs(root, 0);
        return result;
    }

private:
    void dfs(TreeNode* node, int prefixSum)
    {
        if (node == NULL){
            return;
        }

        prefixSum += node->val;
        if (cache.find(prefixSum - sum) != cache.end()){
            result += cache[prefixSum - sum];
        }
        if (cache.find(prefixSum) != cache.end()){
            cache[prefixSum] = cache[prefixSum] + 1;
        }
        else{
            cache.insert({prefixSum, 1});
        }

        dfs(node->left, prefixSum);
        dfs(node->right, prefixSum);
        cache[prefixSum] -= 1;
    }

private:
    int sum;
    int result;
    unordered_map<int, int> cache;
};
