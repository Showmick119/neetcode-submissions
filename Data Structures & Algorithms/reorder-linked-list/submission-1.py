# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the middle pointer ending point
        slow, fast = head, head.next
        while slow and slow.next and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        middle = slow # this is where we will actually stop

        # can't go back through the list, need to change pointers from back to middle
        curr = middle.next
        middle.next = None
        prev = None
        while curr != None: # go from middle to back and keep changing the pointers
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # back pointer
        back = prev

        # starting pointer
        start = head

        while back:
            temp1 = start.next
            temp2 = back.next # now that it's reversed
            back.next = start.next
            start.next = back
            start = temp1
            back = temp2
        return None


"""
- you keep selecting from both ends and placing them here. one from the left side, one from
the right side, and keep putting them together.
- we can get the starting and back pointer. but how do we know when we have reached the end
of the list?
- that's exactly why we need to know the middle pointer using the fast and slow pointers
technique.
- it's the middle pointer if it's an odd number length, and it's the second pointer if it's
an even number length.
- it's a slight variation of the slow and fast pointers problem, as now you wait till fast
goes null, and at that moment, the slow pointers position tells you the middle pointer.
- only really need to check for fast, because if fast is non-null, slow will obviously be
non-null too.
"""