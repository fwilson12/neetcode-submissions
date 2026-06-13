class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        numset = set(nums)
        longest = 0
        for i in range(len(nums) - 1):
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
