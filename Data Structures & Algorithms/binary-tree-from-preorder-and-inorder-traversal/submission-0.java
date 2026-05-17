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
    // inorder and preorder arrays are the same length!
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        // iterative dfs -> find the root from preorder list
        // find the right and left elements from the inorder list
        // passing in a new preorder and inorder array every time
        // but the length of the new arrays are shortened
        if (preorder.length == 0 || inorder.length == 0) {
            return null;
            // TreeNode is an Object, and an Object can be null
        }

        TreeNode root = new TreeNode(preorder[0]);
        // Find it's middle spot in the inorder list, such that you know
        // what's in the left subtree and right subtree of that specific
        // root. We will have several such roots, for main trees, and
        // also for subtrees.
        int mid = -1;
        for (int i = 0; i < inorder.length; i++) {
            if (inorder[i] == preorder[0]) {
                mid = i;
                break;
            }
        }

        // with the knowledge of this midpoint, create new inorder and
        // preorder list. But a seperate one for the left and right
        // portions of the midpoint.
        // Starting from 1, so we skip over the current root.
        int[] leftPreorder = Arrays.copyOfRange(preorder, 1, mid + 1);
        // the left portion of the new subarray, which starts from the
        // previous root's index, all the way to mid in the inorder
        int[] leftInorder = Arrays.copyOfRange(inorder, 0, mid);
        // exclusive and we don't want the mid to be in this new array
        root.left = buildTree(leftPreorder, leftInorder);

        int[] rightPreorder = Arrays.copyOfRange(preorder, mid + 1, preorder.length);
        int[] rightInorder = Arrays.copyOfRange(inorder, mid + 1, inorder.length);
        root.right = buildTree(rightPreorder, rightInorder);
        
        return root;
    }
}
