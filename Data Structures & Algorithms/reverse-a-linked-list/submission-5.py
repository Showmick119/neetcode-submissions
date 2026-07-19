# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        temp = None
        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        head = prev
        return head

"""
- O(1) space is needed, so can't just create another list
- null in Java is None in Python
- you can't make it into a DLL, it has to be solved as an SLL
- using curr, prev and temp pointers are common patterns in LL problems
"""