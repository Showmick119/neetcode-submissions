# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        indexMap = {}
        index = 0
        curr = head # pointer to iterate through the Linked List
        while curr != None:
            indexMap[index] = curr
            index += 1
            curr = curr.next
        length = index
        print(length)
        
        curr = head
        curr.next = indexMap[0]
        index = 1 # with each value X we do two things -> x and n - x, then we move
        while curr != None and index < length:
            curr.next = indexMap[length - index]
            curr.next.next = indexMap[index]
            index += 1
            curr = curr.next
        return head

"""
- do the naive solution first
"""