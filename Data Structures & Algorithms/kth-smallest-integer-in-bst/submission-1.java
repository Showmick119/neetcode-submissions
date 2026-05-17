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
    List<Integer> list;
    public int kthSmallest(TreeNode root, int k) {
        // if we do DFS, then the variable should be instance variable
        // how about I make an ArrayList
        // Collections.min(list), and we do this operation k times
        // and remove k times, till we get the kth smallest value in
        // the ArrayList
        // first traverse and store everything in list
        // INORDER TRAVERSAL IS THE ONE WHICH GIVES SORTED
        // LEVEL ORDER DOES NOT GIVE SORTED, SO CREATE LIST WITH 
        // INORDER TRAVERSAL, AND THEN GET MINIMUM K TIMES IN THAT
        // SORTED LIST
        list = new ArrayList<>();
        traverse(root);  // so now list is created and ready to go

        return list.get(k - 1);
    }

    public void traverse(TreeNode root) {
        if (root == null) {
            return;
        }
        traverse(root.left);
        list.add(root.val);
        traverse(root.right);
        return;
    }
}
