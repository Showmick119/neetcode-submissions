# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        root = self.helper(root)
        return root
    
    def helper(self, node: Optional[TreeNode]) -> None:
        if node == None:
            return
        node.left, node.right = node.right, node.left
        self.helper(node.left)
        self.helper(node.right)
        # after you do all pointer reinforcements, return the original node
        return node
        

"""
- individually invert each subtree
"""