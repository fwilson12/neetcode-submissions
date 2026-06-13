class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            dummyNums = nums[i + 1:]
            if target - nums[i] in dummyNums:
                return [i, nums.index(target - nums[i])]
