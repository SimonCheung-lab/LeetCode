/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    private TreeNode preNode = null;
    private boolean valid = true;

    public boolean isValidBST(TreeNode root) {
        this.valid = true;
        inOrder(root);
        return this.valid;
    }

    private void inOrder(TreeNode node) {
        if (node == null) {
            return;
        }

        inOrder(node.left);

        if (preNode == null) {
            preNode = node;
        }
        else {
            if (preNode.val >= node.val) {
                this.valid = false;
                return;
            }
            else {
                preNode = node;
            }
        }

        inOrder(node.right);
    }
}
