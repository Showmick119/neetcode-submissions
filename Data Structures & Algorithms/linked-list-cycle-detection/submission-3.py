# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        index = 0
        visitMap = {} # (value) : (index)
        seen = set()
        curr = head
        while curr != None:
            if curr.next in seen:
                return True
                # return visitMap[curr.val] # will give its index
            else:
                seen.add(curr)
            curr = curr.next
            index += 1
        return False

"""
- we can trivially keep a hashset, but that goes against the o(1) space complexity
"""