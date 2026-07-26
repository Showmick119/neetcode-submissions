# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def __init__(self):
        self.isSame = True

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        out1 = []
        self.helper(p, out1)
        out2 = []
        self.helper(q, out2)
        if out1 != out2:
            self.isSame = False
        return self.isSame
    
    def helper(self, node: Optional[TreeNode], out: List) -> None:
        if node == None:
            out.append('#')
            return
        else:
            out.append(node.val)
            self.helper(node.left, out)
            self.helper(node.right, out)

"""
- 
"""