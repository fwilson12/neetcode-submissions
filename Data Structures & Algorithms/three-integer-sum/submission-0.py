"""
1. sort nums
2. start i at zero, j = 0 or i + 1 if i is zero, k = len - 1
3. if -nums[i] == nums[j] + nums[k]
    - res.append([nums[i], nums[j], nums[k]])
4. if target > nj + nk
    - increment j to get a bigger sum
5. if target < nj + nk
    - decrement k to get a smaller sum
continue until j !< k
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        res_indices = set()
        nums.sort()
        
        for i in range(len(nums) - 1):
            target = -nums[i]
        
            j = i + 1       
            k = len(nums) - 1
           
            while j < k:            
                curr_sum = nums[j] + nums[k]
                if curr_sum == target and tuple(sorted([i, j, k])) not in res_indices:   
                   res_indices.add(tuple(sorted([i, j, k])))
                   res.append([nums[i], nums[j], nums[k]])
                   j += 1
                   break

                if curr_sum > target:
                    k -= 1
                
                else:
                    j += 1
        
        return res



                    
        