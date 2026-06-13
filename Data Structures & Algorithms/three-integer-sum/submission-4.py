class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen = set()
        nums.sort()

        for i in range(len(nums) - 1):
            target = -nums[i]
        
            j = i + 1       
            k = len(nums) - 1
           
            while j < k:            
                curr_sum = nums[j] + nums[k]
                if curr_sum == target and tuple(sorted([nums[i], nums[j], nums[k]])) not in seen:   
                   seen.add(tuple(sorted([nums[i], nums[j], nums[k]])))
                   res.append([nums[i], nums[j], nums[k]])
                   j += 1
                   

                if curr_sum > target:
                    k -= 1
                
                elif curr_sum < target:
                    j += 1
        
        return res



                    
        