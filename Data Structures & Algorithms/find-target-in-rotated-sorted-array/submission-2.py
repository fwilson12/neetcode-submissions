class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        iL = 0
        iR = len(nums) - 1
        
        pivIdx = 0

        # find pivot (minimum)
        while iL <= iR:

            iM = iL + (iR - iL) // 2

            # If the current range is sorted, iL is the pivot
            if nums[iL] <= nums[iR]:
                pivIdx = iL
                break

            # If mid is greater than or equal to left, the pivot is in the right half
            if nums[iM] >= nums[iL]:
                iL = iM + 1
            # Otherwise, the pivot is in the left half (including mid)
            else:
                pivIdx = iM
                iR = iM - 1


        # now we have split the list to [:pivot] and [pivot:]
        
        if target == nums[pivIdx]:
            return pivIdx

        # search right segment
        L, R = pivIdx, len(nums) - 1
        # if target is within bounds of left segment, update search range
        if pivIdx > 0 and target >= nums[0] and target <= nums[pivIdx - 1]:
            L, R = 0, pivIdx - 1
            
        while L <= R:
            M = L + (R - L) // 2

            if target == nums[M]:
                return M
            
            elif  target > nums[M]:
                L = M + 1
            
            else:
                R = M - 1
        return -1