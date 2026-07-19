# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False

"""
- we can trivially keep a hashset, but that goes against the o(1) space complexity
- each node has only one pointer
- so the cycle can only possibly be from the tail node to some node in the middle
"""