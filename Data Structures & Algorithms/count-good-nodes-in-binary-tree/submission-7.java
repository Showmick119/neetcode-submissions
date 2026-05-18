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

    [4, 1, 3]: 3 is greater than 1, but is condition met? NO. It must be
    greater than everything in path. So that also includes the number
    before 1, that being 4. Since 3 < 4, 3 is not a good Node. Hence,
    to keep track, it is best to store maximum. Cause, if Node is
    greater than maximum, than it's greater than everything in that
    path.

    Additionally, should keep it seperate for left and right. Don't make
    maxVal a global variable. Should be specific to the path. Hence,
    better to pass it in as a parameter/argument to the function.

    Preorder traversal
    */

    public int goodNodes(TreeNode root) {
        return dfs(root, root.val);
    }
    
    // Treating each Node as a seperate root. So give it the maxValue
    // till that point.
    private int dfs(TreeNode root, int maxVal) {
        if (root == null) {
            return 0;
        }

        int count = (root.val >= maxVal) ? 1 : 0;
        maxVal = Math.max(maxVal, root.val);
        count += dfs(root.left, root.val);
        count += dfs(root.right, root.val);
        return count;
    }
}
