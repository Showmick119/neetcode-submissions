# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def __init__(self):
        self.balanced = True

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        temp = self.helper(root)
        return self.balanced
    
    def helper(self, node: Optional[TreeNode]) -> int:
        if node == None:
            return 0
        height = 0
        leftHeight = self.helper(node.left)
        rightHeight = self.helper(node.right)
        if abs(leftHeight - rightHeight) > 1:
            self.balanced = False
        return 1 + max(leftHeight, rightHeight)


"""
- check each and every node individually
- chain of thought is that each node should be treated like its own individual subtree with
all necessary properties like height, width, etc.
"""