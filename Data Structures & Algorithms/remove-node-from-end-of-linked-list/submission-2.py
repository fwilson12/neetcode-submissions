# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        

        # give ptr 2 a head start (n nodes ahead of ptr1)
        ptr2 = head
        for i in range(n):
            ptr2 = ptr2.next

        # use ptr2 as a feeler for the end of the list. 
        # when ptr2 reaches null, ptr1 is the nth node from the end of the list
        prev = None
        ptr1 = head
        while ptr2:
            prev = ptr1
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        # removing first node from list
        if prev is None: 
            head = head.next
        # remove link to node at ptr1
        else:
            prev.next = prev.next.next 


        return head

