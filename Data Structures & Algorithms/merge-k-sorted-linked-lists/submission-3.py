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

        while True:
            
            nodeHeap = [] # list of (index, value) | we need an index to fetch the curr head of the LList we're updating
            for i in range(len(lists)):
                if not lists[i]:
                    continue
                else: 
                    heapq.heappush(nodeHeap, (lists[i].val, i))

            if not nodeHeap:
                break
            
            curr.next = lists[nodeHeap[0][1]]
            lists[nodeHeap[0][1]] = lists[nodeHeap[0][1]].next
            curr = curr.next

        return dummy.next


