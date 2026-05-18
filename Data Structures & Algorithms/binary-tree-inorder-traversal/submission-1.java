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
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> list = new ArrayList<>();
        // preorder - CLR
        // inorder - LCR
        // postorder - LRC
        if (root == null) {
            return list;
        }
        inorderTraversal(root.left);
        list.add(root.val);
        inOrderTraversal(root.right);
        return list;
    }
}