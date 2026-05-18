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
    /*
    If it's greater than the Max, then it's also greater than the Node
    before it. Using max is a good way of keeping track, that the
    current Node is greater than all that came before it.
    */
    int count = 0;
    int maxVal = 0;

    public int goodNodes(TreeNode root) {
        maxVal = root.val;
        dfs(root);
        return count;
    }

    private void dfs(TreeNode root) {
        if (root == null) {
            return;
        }
        
        count += (root.val > maxVal) ? 1 : 0; // current root greater than previous
        maxVal = Math.max(maxVal, root.val);
        count += dfs(root.left);
        count += dfs(root.right);
    }
}
