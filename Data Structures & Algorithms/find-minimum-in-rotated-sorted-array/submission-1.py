class Solution:
    def findMin(self, nums: List[int]) -> int:
        

        lIdx = 0
        rIdx = len(nums) - 1

        while lIdx <= rIdx:
            midIdx = lIdx + (rIdx - lIdx) // 2
            
            l = nums[lIdx]
            m = nums[midIdx]
            r = nums[rIdx]
            # left value is min, no possible smaller values
            if l <= m and l <= r: # account for size 1
                return l

            # right val is min, possible mins are between midIdx + 1 (m wasn't the min) and r
            elif r < l and r < m or l == m:
                lIdx = midIdx + 1

            else:
                rIdx = midIdx
           

            

