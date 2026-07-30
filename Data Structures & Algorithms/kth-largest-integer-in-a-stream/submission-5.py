import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        self.kth = None
        # heapify nums in place, pop down to only largest k
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
            return self.heap[0]
        
        topVal = self.heap[0]

        # if newVal is smaller than the kth largest nothing changes
        if val < topVal:
            return topVal
        
        # old largest is out, insert new val and return the new kth largest
        else:
            heapq.heappushpop(self.heap, val)
            return self.heap[0]
        

