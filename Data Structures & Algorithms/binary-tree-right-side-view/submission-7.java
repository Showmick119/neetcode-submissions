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
    List<Integer> list = new ArrayList<>();

    public List<Integer> rightSideView(TreeNode root) {
        dfs(root, 0);
        return list;
    }

    private void dfs(TreeNode node, int depth) {
        if (node == null) {
            return;
        }

        /* 
        Any subsequent nodes at the same depth (from the left subtree) 
        won't be added because the list already has an element at that 
        depth.
        */
        if (list.size() == depth) {  // only adding the first node encountered at each depth
        // the left is mainly for, if a right doesn't exist. Then in that case
        // the rightmost exists in the left subtree. Depth would have updated
        // by the time of the 2nd iteration.
            list.add(node.val);
        }

        dfs(node.right, depth + 1);
        dfs(node.left, depth + 1);

        /*
        Only add the first node you encounter at each depth (since 
        you're going right-first, this will be the rightmost) 
        */
    }
}
