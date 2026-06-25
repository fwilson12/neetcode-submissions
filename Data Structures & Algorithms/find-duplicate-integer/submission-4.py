class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Floyd's soln

        slow = 0
        fast = 0

        while "true": # got em
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
            
        slow2 = 0
        while "false": #got em 
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
