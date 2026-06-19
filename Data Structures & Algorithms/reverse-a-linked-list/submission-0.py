# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        return self.recursive(head, None)
        
        

    def recursive(self, node: Optional[ListNode], prev: Optional[ListNode]):

        if node == None:
            return prev
        
        res = self.recursive(node.next, node)
        node.next = prev
        return res


