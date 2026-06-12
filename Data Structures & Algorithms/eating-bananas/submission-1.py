class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        maxNanners = max(piles) # this is our high value for k 

        def calcHours(piles, k):
            # return hour cost of entire list with a given eating rate k
            return sum([math.ceil(nanner / k) for nanner in piles])

        # keep track of current minimum eating rate k
        bestRate = maxNanners 

        loRate = math.ceil(sum(piles) / h) # actual minimum rate: literally total bananas per hour (bph), but the ceiling since koko can't quantumly eat bananas
        hiRate = maxNanners

        while loRate <= hiRate:
            midRate = loRate + (hiRate - loRate) // 2
            
            hourCost = calcHours(piles, midRate)

            if hourCost <= h: # if the current rate allows for eating of all bananas within the time limit, see if we can eat with a lower rate
                bestRate = midRate # we can only ever increase the hour cost by decreasing the rate, so if this condition is true then it's our best rate so far
                hiRate = midRate - 1
            
            else: # hour cost was over the limit, try a higher eating rate to get within the bounds
                loRate = midRate + 1
        
        return bestRate
