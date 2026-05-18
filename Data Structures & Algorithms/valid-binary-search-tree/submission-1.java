/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public boolean isValidBST(TreeNode root) {
        // Check that every Node follows the property of left smaller
        // and right greater. If BST property broken above, then the
        // rest of the tree doesn't even need to be checked.
        if (root == null) {
            return true;
        }
        if (root.right > root.val && root.left < root.val) {
            isValidBST(root.left);
            isValidBST(root.right);
        } else {
            return false;
        }
    }
}
