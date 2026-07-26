# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None: # empty list, with no Tree Nodes
            return 0
        from collections import deque
        queue = deque()
        queue.append((root, 0))
        size = self.helper(root, queue)
        return size
    
    def helper(self, node: Optional[TreeNode], queue) -> int:
        while len(queue) > 0:
            curr, size = queue.popleft()
            if curr != None:
                size += 1
                queue.append((curr.left, size))
                queue.append((curr.right, size))
        return size