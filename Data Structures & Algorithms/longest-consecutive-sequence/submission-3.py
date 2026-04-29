class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0
        for num in nums:
            curr_seq = 1
            if num - 1 not in numset:
                curr_num = num
                while curr_num + 1 in numset:
                    curr_seq += 1
                    curr_num += 1 
            
            longest = max(longest, curr_seq)
        
        return longest
