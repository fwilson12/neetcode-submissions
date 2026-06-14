class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        small, big = nums1, nums2 # assume nums1 is shorter for now
        elems = len(nums1) + len(nums2) 
        half = elems // 2

        # correct the size of the arrays
        if len(big) < len(small):
            small, big = big, small

        L, R = 0, len(small) - 1

        while 1: # guranteed to find a result

            midSmall = L + (R - L) // 2 # index of last element we're taking from small array
            midBig = half - midSmall - 2 # index of the last element we're taking from big array, adjusted for converting a discrete sum (half) to indices (- 2, -1 for each subarray)

            smallLeft = small[midSmall] if midSmall >= 0 else float("-infinity") # largest value in small left subarray
            smallRight = small[midSmall + 1] if midSmall + 1 < len(small)  else float("infinity") # smallest value in small right subarray
            bigLeft = big[midBig] if midBig >= 0 else float("-infinity") # largest value in big left subarr
            bigRight = big[midBig + 1] if midBig + 1 < len(big) else float("infinity") # smallest value in big right subarr


            # split is valid, all elements up to bigLeft/smallLeft <= all elements including and after bigRight/smallRight
            if smallLeft <= bigRight and bigLeft <= smallRight:
                # odd elems
                if elems % 2 != 0:
                    return min(smallRight, bigRight) # smaller value between the smallest value of right subarrays, will be on right side since the halfway point is rounded down

                return (max(smallLeft, bigLeft) + min(smallRight, bigRight)) / 2 # average of two middle values in merged array

            elif smallLeft > bigRight: # if the biggest value in small left subarray is greater than the smallest value of the big right subbary, we need fewer values in small left subarray
                R = midSmall - 1
            
            else: # smallRight > bigLeft: the biggest value in the left big subarray is greater than the smallest value of the small right subarray; we need more values in the small subarray and fewer in the big subbary
                L = midSmall + 1



