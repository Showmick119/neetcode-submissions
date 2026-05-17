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
    boolean balanced = true;

    public boolean isBalanced(TreeNode root) {
        /*
        This method returns boolean, and we need a recursive method
        to return int so we can calculate left and right heights.

        A Binary Tree is balanced if every node's left and right 
        subtrees have heights differing by at most 1.

        It's not just about the root - the balance condition must 
        hold for all nodes in the tree.
        */
        height(root);
        return balanced;
    }

    // do the left and right height check for EACH and every Node
    public int height(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int left = height(root.left);
        int right = height(root.right);

        if (Math.abs(left - right) > 1) {
            balanced = false;
        }

        return 1 + Math.max(left, right);
    } 
}
