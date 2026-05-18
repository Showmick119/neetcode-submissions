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
    int count = 0;

    public int goodNodes(TreeNode root) {
        dfs(root);
        return count;
    }

    public void dfs(TreeNode root) {
        if (root == null) {  // to terminate counting and start going up
            return;
        }
        if (root.left.val > root.val) {
            count++;
            dfs(root.left);
        } else if (root.right.val > root.val) {
            count++;
            dfs(root.right);
        } else {
            dfs(root.left);
            dfs(root.right);
        }
    }
}
