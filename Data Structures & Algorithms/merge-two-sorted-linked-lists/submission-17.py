# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3 = dummy = ListNode()
        
        while list1 and list2:
            if list1.val <= list2.val:
                list3.next = list1
                list1 = list1.next
            else:
                list3.next = list2
                list2 = list2.next
            list3 = list3.next

        list3.next = list1 or list2 # whichever is not-None (non-False) will get assigned here

        return dummy.next # where the ListNode() actually starts


"""
- in this problem there's no need for o(n) space
- you can do it in o(1) by just utilizing all existing pointers
"""