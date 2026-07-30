# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.answer = False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        out1 = []
        self.helper(root, out1)
        out2 = []
        self.helper(subRoot, out2)
        self.slidingWindow(out1, out2)
        return self.answer
    
    def helper(self, node: Optional[TreeNode], out: List) -> None:
        if node == None:
            out.append(None)
            return
        # post order traversal
        self.helper(node.left, out)
        self.helper(node.right, out)
        out.append(node.val)
    
    def slidingWindow(self, mainList: List, subList: List) -> None:
        from collections import deque
        subDeque = deque(subList)
        w = deque()
        for r in mainList:
            if len(w) == len(subDeque):
                if w == subDeque:
                    self.answer = True
                else:
                    w.popleft()
            w.append(r)
        if len(w) == len(subDeque):
            if w == subDeque:
                self.answer = True

"""
- rule of thumb, treat every single node as an individual subtree.
- the inputs seem like they have been pulled out through a BFS pattern.
- check when the length is equal for a specific subtree.
"""