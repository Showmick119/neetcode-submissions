# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None # edge case
        dummy = node = ListNode()
        while list1 and list2:
            if list1.val < list2.val: # we process and get rid of the smallest values
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next # won't throw NPE, as we are never None, and always pointing to an
            # existing list with continuing chained Nodes/values
        node.next = list1 or list2 # not a single
        return dummy.next # the head of the node list we just created without introducting a 
        # brand new list number 3!
        # dummy was also pointing to the same thing node was. but node went on and built the
        # whole linked list, while dummy was left behind and kept pointing at the dummy. but
        # dummy.next pointed to the head of the list which node iteratively created. so dummy
        # was actually holding the head of the linked list all along.

"""
- returning the head of a LL, returns the LL itself
"""