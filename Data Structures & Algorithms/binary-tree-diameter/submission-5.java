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
    public int max;

    public int diameterOfBinaryTree(TreeNode root) {
        /*
        We want to return height of each Node. But we also want to
        calculate and keep track of the diameter property, which is
        just the left height + the right height. We will calculate
        both the height and the diameter of EVERY NODE. We
        are treating each Node as the root of it's own subtree
        with a left and right child, which determine both its height
        and its diameter.
        */
        if (root == null) {
            return -1;
        }

        int left = diameterOfBinaryTree(root.left);
        int right = diameterOfBinaryTree(root.right);
        max = Math.max(max, left + right); // updating diameter
        return 1 + Math.max(left, right);
    }
}
