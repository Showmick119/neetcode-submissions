# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        length = 0
        while curr != None:
            curr = curr.next
            length += 1
        
        if length == 1 and n == 1:
            return None

        curr = head
        index = 0
        targetIndex = length - n
        while curr != None:
            if index == targetIndex - 1:
                curr.next = curr.next.next
                curr = curr.next.next
                continue
            curr = curr.next
            index += 1
        return head

"""
- nth node from the end of the list, not from the front
- first go to the back, and then from there, go n steps front, and remove that specific node
in place
- do one pass where you find and check the length of the linked list, and then do another
pass where you iterate X amount of times, where X = length - n, where n is the passed in
parameter for the question
"""