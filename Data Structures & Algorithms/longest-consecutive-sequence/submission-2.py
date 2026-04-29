class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        numset = set(nums)
        longest = 1
        for i in range(len(nums)):
            curr_seq = 1
            
            if nums[i] - 1 in numset:
                continue
            
            else:
                curr_num = nums[i]
                while curr_num + 1 in numset:
                    curr_seq += 1
                    curr_num += 1 
            
            if curr_seq > longest:
                longest = curr_seq
        
        return longest
