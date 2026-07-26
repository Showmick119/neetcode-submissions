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
        queue.append(root)
        size = self.helper(root, queue, 1)
        return size
    
    def helper(self, node: Optional[TreeNode], queue, size : int) -> int:
        while len(queue) > 0:
            curr = queue.popleft()
            if curr.left != None and curr.right != None:
                queue.append(curr.left)
                queue.append(curr.right)
                size += 1
            elif curr.left != None:
                queue.append(curr.left)
                size += 1
            elif curr.right != None:
                queue.append(curr.right)
                size += 1
        return size