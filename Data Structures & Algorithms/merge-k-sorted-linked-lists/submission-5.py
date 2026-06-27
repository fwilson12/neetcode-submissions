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


        nodeHeap = [] 
        # add first node in each list to our heap
        for i, node in enumerate(lists):
            if node is None: continue

            heapq.heappush(nodeHeap, (node.val, i, node)) # need i for ties in node.val, but really just sorting by val, need ref to node
                
        # we're done when each node is pushed and popped 
        while nodeHeap:
            # heap[0] is min node
            val, i, node = heapq.heappop(nodeHeap)
            # link node to res, then advance ptr within node's list 
            curr.next = node
            node = node.next
            curr = curr.next

            # push the next node of the kth list we removed from if it exists
            if node:
                heapq.heappush(nodeHeap, (node.val, i, node))

            
            
        return dummy.next


