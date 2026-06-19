import heapq


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        # init window heap (O(k))
        winHeap = []
        for i in range(k):
            # need max heap, so most positive number would be at bottom; negate it to ensure it's at the top of heap.
            heapq.heappush(winHeap, (-nums[i], i)) # add as value, index tuples for reference later

        L = 0
        res = []
        # R is the last element in the current window. 
        for R in range(k, len(nums)):

            # pop until max is in the (previous) window 
            while winHeap[0][1] not in range(R - k, R):
                heapq.heappop(winHeap)

            # max is now guranteed to be in the window
            res.append(-winHeap[0][0])

            # for next iter:
            heapq.heappush(winHeap, (-nums[R], R))
        
        # leftover iter
        while winHeap[0][1] not in range(len(nums) - k, len(nums)):
                heapq.heappop(winHeap)
        res.append(-winHeap[0][0])


        return res

        