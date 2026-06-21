# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
    
        # find midpoint: slow will land on last element in first half 
        fast = head
        slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # store ref so we can iterate after we reverse second half
        back = slow.next
        slow.next = None # separate

        # reverse ts
        prev = None
        curr = back
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        back = prev

        # combine these jawns
        res = head
        curr = head
        front = head.next
        while front and back: # front will reach null, as slow.next is now null 
            
            curr.next = back
            back = back.next
            curr = curr.next

            curr.next = front
            front = front.next
            curr = curr.next

        # front will always exhaust, back may have a leftover
        if back:
            curr.next = back

        head = res



    