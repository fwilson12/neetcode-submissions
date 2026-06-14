class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxSum = nums[0]
        currSum = 0
        for num in nums:
            # start new subarray if currSum is negative, as any subarray beginning with a negative number is strictly less than a new subarray with the number after
            currSum = max(0, currSum)
            currSum += num
            maxSum = max(maxSum, currSum) # handles all-negative arrays
        
        return maxSum


'''
[-2, -4, -1212, -1]
'''