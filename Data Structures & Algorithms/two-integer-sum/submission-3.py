class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapThing = {}
        for i in range(len(nums)):
            if target - nums[i] in mapThing:
                return [mapThing.get(target - nums[i]), i]
            else:
                mapThing[nums[i]] = i

