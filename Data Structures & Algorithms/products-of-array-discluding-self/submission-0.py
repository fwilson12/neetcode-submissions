from functools import reduce
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            newnums = nums[:i] +  nums[i+1:]
            res.append(reduce(lambda x, y: x * y, newnums))
        return res
        

