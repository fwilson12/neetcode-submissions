# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head: return None
        
        res = None
        
        # curr is the head of its group, nextDude is the head of the next group. 
        curr = head
        nextDude = head
        prevTail = None # the new tail of the group we just reversed; is always the head of its original group

        reversing = True
        while reversing:
            # send out nextDude, cancel if the group is incomplete
            for i in range(k):
                if nextDude is None:
                    reversing = False
                    break
                nextDude = nextDude.next
            
            if not reversing: break

            # reverse the linked list from [curr, nextDude). newHead is the new head of the reversed LL; it was once the tail, now it's the head. yeah.
            # if we're past the first iteration, we'll need to link the last group to this one. this means linked the previous tail to the new head. intuitive
            newHead = self.reverseLL(curr, nextDude)
            
            
            if res is None: # if this is the first iteration. used to return the SUPER head (tail of first group)
                res = newHead
            if prevTail is not None: # if we're not reversing the first group, link the previous group's tail to the new head
                prevTail.next = newHead

            prevTail = curr # prevTail is now the node that WILL be the tail of its group after reversal, or the head of an incomplete (not reversed) group
            curr = nextDude # move curr up to newDude and repeat

        return res


    # might as well write the comment for this one in mandarin should go without saying
    def reverseLL(self, head, nextHead):

        prev = nextHead
        curr = head
        while curr and curr is not nextHead:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev