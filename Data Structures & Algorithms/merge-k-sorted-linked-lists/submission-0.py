# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



# this soln was too easy for this to be a hard problem, will re-do later 
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        dummy = ListNode()
        curr = dummy


        while True:
            smallest = 100000
            smallIdx = -1
            for i, node in enumerate(lists):
                if not node or node.val > smallest:
                    continue
                else:
                    smallest = node.val
                    smallIdx = i 
            if smallIdx == -1:
                break
            curr.next = lists[smallIdx]
            curr = curr.next
            lists[smallIdx] = lists[smallIdx].next


        return dummy.next
