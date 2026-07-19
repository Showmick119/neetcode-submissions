# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return ListNode()
        list3 = ListNode()
        curr3 = list3 # Node with (val=0, nextNode=None)
        curr1 = list1
        curr2 = list2
        prev = ListNode() # necessary since its an SLL
        while curr1 != None and curr2 != None:
            if curr1.val <= curr2.val:
                prev = curr3
                curr3.val = curr1.val
                newNode = ListNode()
                curr3.next = newNode
                curr3 = curr3.next
                curr1 = curr1.next
            else:
                prev = curr3
                curr3.val = curr2.val
                newNode = ListNode()
                curr3.next = newNode
                curr3 = curr3.next
                curr2 = curr2.next
        if curr1 == None and curr2 != None:
            while curr2 != None:
                prev = curr3
                curr3.val = curr2.val
                newNode = ListNode()
                curr3.next = newNode
                curr3 = curr3.next
                curr2 = curr2.next
        elif curr2 == None and curr1 != None:
            while curr1 != None:
                prev = curr3
                curr3.val = curr2.val
                newNode = ListNode()
                curr3.next = newNode
                curr3 = curr3.next
                curr1 = curr1.next
        prev.next = None
        return list3

"""
- returning the head of a LL, returns the LL itself
"""