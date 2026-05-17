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

        // since array is 0-indexed, asking for k = 1, actually gives us
        // the 2nd smallest element not the 1st, since index 1 has the
        // 2nd smallest. So to get 1st smallest, user can pass in k = 1,
        // but we have to send (k - 1), such that we can get 1 - 1 = 0
        // index of the array, the smallest element as intended.
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
