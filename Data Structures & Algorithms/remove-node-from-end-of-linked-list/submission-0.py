# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        res = prev

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

        else:
            prev.next = curr.next

        prev = None
        curr = res
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
            