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
    public TreeNode deleteNode(TreeNode root, int key) {
        // if present, meanin it is not guaranteed to be present
        // must return root Node reference for pointer reinforcement,
        // regardless of if an update was made or not.
        // 3 cases for removal. 0 children, 1 child, 2 children
        if (root == null) {
            return null;
        }
        if (key > root.val) {
            root.right = deleteNode(root.right, key);
        } else if (key < root.val) {
            root.left = deleteNode(root.left, key);
        } else {
            // now we have reached the Node we want to remove, now we
            // have to consider all the different removal cases
            // Single Child
            if (root.left == null) {
                return root.right;  // this can also be null, so it
                // could also work for ZERO-CHILD CASE
                // essentially replacing the single child Node by
                // skipping over that Node and pointing directly to
                // it's child
            } else if (root.right == null) {
                return root.left; // this can also be null, so it
                // could also work for ZERO-CHILD CASE
            } else {
                // the special two-child case
                // we want successor, so right subtree's SMALLEST VALUE
                // SO PASS IN root.right, but then we get it's minimum
                // root.left value
                TreeNode minNode = getMinNode(root.right, key);
                root.val = minNode.val; // get the minNode and then put it's value
                // don't be putting the value of the right Node, as that
                // is not the successor
                root.right = deleteNode(root.right, minNode.val);
                // have to specifically delete the minimum value from
                // that right subtree
            }
        }
        return root;
    }

    public TreeNode getMinNode(TreeNode root) {
        TreeNode curr = root;
        while (curr != null && curr.left != null) {
            curr = curr.left;
        }
        return curr;
    }
}