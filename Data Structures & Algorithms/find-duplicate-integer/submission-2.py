class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        
        ptr = 0
        while 1:
            nums[ptr] *= -1

            if nums[ptr] > 0:
                return ptr
            
            ptr = abs(nums[ptr])
              

        

