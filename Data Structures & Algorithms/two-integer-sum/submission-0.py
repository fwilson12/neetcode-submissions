class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(set(nums))):
            if target - nums[i] in nums:
                return [i, nums.index(target - nums[i])]
