# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def __init__(self):
        self.diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        temp = self.helper(root, 0)
        return self.diameter
    
    def helper(self, node: Optional[TreeNode], length : int = 0) -> int:
        if node != None:
            length = 0
            leftHeight = self.helper(node.left, length)
            rightHeight = self.helper(node.right, length)
            self.diameter = max(self.diameter, leftHeight + rightHeight)
            length = max(leftHeight, rightHeight) + 1
            return length
        else:
            return 0

"""
- diameter is calculating left + right height at every single node. this is how you get the 
diameter, by using subtree heights and widths.
- for getting things like heights we need postorder traversal
- we keep calculating height from the bottom and keep passing it up.
"""