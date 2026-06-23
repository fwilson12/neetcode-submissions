# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not l1 or not l2:
            return None

        # to be returned
        dummy = ListNode()
        res = dummy

        # elementary school addition this needs no explanation
        carry = 0
        while l1 and l2:
            currSum = l1.val + l2.val + carry
            carry = 1 if currSum > 9 else 0
            dummy.next = ListNode(currSum % 10)
            dummy = dummy.next
            l1 = l1.next
            l2 = l2.next

        # jagged input
        while l1:
            currSum = l1.val + carry
            carry = 1 if currSum > 9 else 0
            dummy.next = ListNode(currSum % 10)
            dummy = dummy.next
            l1 = l1.next

        # ^^^
        while l2:
            currSum = l2.val + carry
            carry = 1 if currSum > 9 else 0
            dummy.next = ListNode(currSum % 10)
            dummy = dummy.next
            l2 = l2.next
        
        # extra node if there's an extra carry why is this even a comment just read the code
        if carry:
            dummy.next = ListNode(1)

        return res.next