class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # start point at first elem, go from there. Since all(nums) in [1. n], we'll never return here, but the value it points at could be reached again, meaning it's the dupe
        ptr = 0
        while 1:
            # turn the current value negative
            nums[ptr] *= -1

            # if the value was already negative, the value we were just at (ptr) is the duplicate, as we've been directed here before
            if nums[ptr] > 0:
                return ptr
            
            # update the pointer (abs of current value)
            ptr = abs(nums[ptr])
              

        

