class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myset = set(nums)
        if len(myset) == len(nums):
            return False
        return True