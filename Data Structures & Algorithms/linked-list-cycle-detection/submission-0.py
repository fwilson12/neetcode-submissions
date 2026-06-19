# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # you can hash objects
        visited = set()
        curr = head
        
        # will either find a cycle or will reach null
        while curr is not None:
            if curr in visited:
                return True
            
            visited.add(curr)
            curr = curr.next

        return False