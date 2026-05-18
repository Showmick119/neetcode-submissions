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
        return valid(root, Integer.MIN_VALUE, Integer.MAX_VALUE);
    }

    private boolean valid(TreeNode root, int left, int right) {
        if (root == null) {
            return true;
        }
        if ((root.val <= left && root.val >= right)) {
            return false;
        }
        return valid(root.left, left, root.val) && valid(root.right, root.val, right);
    }
}
