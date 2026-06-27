# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # heap soln, off the dome
        if not lists: return None

        dummy = ListNode()
        curr = dummy


        nodeHeap = [] # heap of (val, idx) | we need an index to fetch the curr head of the LList we're updating
        for i, node in enumerate(lists):
            if node is None: continue

            heapq.heappush(nodeHeap, (node.val, i, node)) # need i for ties in node.val
                
        while nodeHeap:
            val, i, node = heapq.heappop(nodeHeap)
            curr.next = node
            node = node.next
            curr = curr.next

            if node:
                heapq.heappush(nodeHeap, (node.val, i, node))

            
            
        return dummy.next


