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
        slow.next = None  # separate

        # reverse ts
        prev = None
        while back:
            next = back.next
            back.next = prev
            prev = back
            back = next
        back = prev

        # combine these jawns
        
        front = head
        while front and back:  # front will reach null, as slow.next is now null
            nextFront, nextBack = front.next, back.next

            front.next = back
            back.next = nextFront

            front = nextFront
            back = nextBack

        # front will always exhaust, back may have a leftover
        if back:
            front.next = back

        
