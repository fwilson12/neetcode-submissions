from functools import reduce
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        
        product_before = 1
        for i in range(len(nums)):
            res[i] = product_before
            product_before *= nums[i]
        
        product_after = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= product_after
            product_after *= nums[i]

        return res