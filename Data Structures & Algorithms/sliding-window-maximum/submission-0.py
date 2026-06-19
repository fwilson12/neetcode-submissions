import heapq


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        # init window heap (O(k))
        winHeap = []
        for i in range(k):
            # need max heap, so most positive number would be at bottom; negate it to ensure it's at the top of heap
            heapq.heappush(winHeap, -nums[i]) 

        L = 0
        res = []
        # R is the last element in the current window. 
        for R in range(k, len(nums)):

            # add max from last window to res
            res.append(-winHeap[0])

            # didn't realize this doesn't work until now :(
            heapq.heappush(winHeap, -nums[R])
            winHeap.remove(-nums[L])
            heapq.heapify(winHeap)
            L += 1

        
        
        res.append(-winHeap[0])
        return res

        