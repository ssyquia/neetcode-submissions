# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        first = list1
        second = list2
        res = ListNode()
        if first is None:
            return second
        if second is None:
            return first 

        tail = res
        while first and second:
            if(first.val <= second.val):
                tail.next = first
                first = first.next
            else:
                tail.next = second
                second = second.next
            tail = tail.next
        
        if first is None: tail.next = second
        else: tail.next = first
        
        return res.next