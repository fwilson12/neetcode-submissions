class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        maxMargin = 0
        L = 0
        for R in range(1, len(prices)):
            
            currMargin = prices[R] - prices[L]
            
            # if currMargin is negative, the R value is less than the L value, meaning every value greater to the right of R will see a higher yield with R as its left (buying) value
            while currMargin <= 0 and L < R:
                L += 1
            
            maxMargin = max(maxMargin, currMargin)

        return maxMargin