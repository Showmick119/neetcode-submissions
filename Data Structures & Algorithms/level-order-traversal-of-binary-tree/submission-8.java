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
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        Deque<TreeNode> queue = new ArrayDeque<TreeNode>();
        if (root != null) {
            queue.addLast(root);
            // List<Integer> temp = new ArrayList<>();
            // temp.add(root.val);
            // res.add(temp);
        }
        int level = 0;
        while (!queue.isEmpty()) {
            int levelLength = queue.size();  // number of elements in the level
            List<Integer> sub = new ArrayList<>();
            for (int i = 0; i < levelLength; i++) {
                TreeNode curr = queue.removeFirst();  // popping then adding children (BOTH LEFT AND RIGHT)
                // it's being popped from queue but it's still part of Tree structure
                sub.add(curr.val);
                if (curr.left != null) {
                    queue.addLast(curr.left);
                    // sub.add(curr.left.val);
                }
                if (curr.right != null) {
                    queue.addLast(curr.right);
                    // sub.add(curr.right.val);
                }
            }
            res.add(sub);
            level++;
        }
        return res;
    }
}
