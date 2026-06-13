class Solution:
    def findMin(self, nums: List[int]) -> int:
        

        lIdx = 0
        rIdx = len(nums) - 1

        while lIdx <= rIdx:
            midIdx = lIdx + (rIdx - lIdx) / 2
            

            # base case
            if nums[lIdx] < nums[midIdx] and nums[lIdx] < nums[rIdx]:
                return nums[lIdx]
           
            # min sorted segment is to the right of mid (right val is greater than left val here)
            elif nums[lIdx] < nums[mid]:
                lIdx = mid + 1

            # left is 
            else:
                rIdx

            

