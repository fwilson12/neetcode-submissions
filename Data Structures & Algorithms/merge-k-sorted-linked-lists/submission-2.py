# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists:
            return None
        
        # keep merging until we have one list node remaining
        while len(lists) > 1:
            merged = []


            # merge all pairs of two lists currently in lists
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None # could be OOB
                # merged will eventually contain every node from lists, but will contain half the head nodes (half the lists)
                merged.append(self.mergeLists(l1, l2))
            lists = merged # update lists, now contains half the lists as the prev iter
        return lists[0] # only 1 head remains

    # goes without saying
    def mergeLists(self, l1, l2):
        if l2 is None: return l1

        dummy = ListNode()
        curr = dummy

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2

        return dummy.next

