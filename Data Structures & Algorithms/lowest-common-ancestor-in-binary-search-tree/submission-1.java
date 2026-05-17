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
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        /* 
        Ancestor allowed to be a descendant of itself.
        Not any ancestor. Must specifically be the lowest.
        All values of the BST are unique.
        Iteration better since recursion has linear space complexity.
        */
        TreeNode curr = root;
        while (curr != null) {
            if (p.val > curr.val && q.val > curr.val) {
                curr = curr.right;
            } else if (p.val < curr.val && q.val < curr.val) {
                curr = curr.left;
            } else {
                return curr;
            }
        }
        return null; // have to still return something
        // TreeNode is an Object and we can always return null for Object
    }

    /*
    Why it's the lowest:
    Once you find the split point, you stop immediately. You can't go any lower because:

    Going left would leave q behind (if q is on the right)
    Going right would leave p behind (if p is on the left)

    The first node where they diverge is automatically the lowest common ancestor.
    Example: root = [5,3,8,1,4,7,9], p = 1, q = 4

    At 5: both < 5 → go left
    At 3: 1 < 3 but 4 > 3 → split! Return 3 (can't go lower)
    */
}
