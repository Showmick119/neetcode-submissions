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
    public int max = 0;

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

        /*
        Need a seperate method, as this one is strictly for returning
        diameter, so we cannot be returning height, since it's very
        different.
        */

        /* 
        The key for this question was just understanding what diameter
        really means in trees.
        */
        height(root);
        return max;
    }

    private int height(TreeNode root) {
        if (root == null) {
            return 0;
        }

        int left = height(root.left);
        int right = height(root.right);
        max = Math.max(max, left + right); // updating diameter
        return 1 + Math.max(left, right);
    }
}
