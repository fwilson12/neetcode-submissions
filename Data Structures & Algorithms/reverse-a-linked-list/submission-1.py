# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # will eventually reference last element. note that this will also set head's next to none, which is the intended behavior (new last elem)
        return self.recursive(head, None)
        
        
    # recursive helper
    def recursive(self, node: Optional[ListNode], prev: Optional[ListNode]):

        # this means prev is the last element in the list; return it so the new head carries through the recursive stack
        if node == None:
            return prev
        
        # store reference to the new head (old last element)
        res = self.recursive(node.next, node)
        # point the current node at it's old node; for the first element, it will point at None
        node.next = prev
        # keeping track of new head 
        return res


