# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        

        # reverse ts
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        res = prev

        # find currNode we're removing, keep track of prev to skip over curr
        prev = None
        curr = res
        nodeNum = 1
        while nodeNum < n:
            prev = curr
            curr = curr.next
            nodeNum += 1

        # removing first element
        if not prev:
            res = res.next
        # break link to curr
        else:
            prev.next = curr.next

        # I'm crine son we're reversing ts again
        prev = None
        curr = res
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
            