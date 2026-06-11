class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        active_heights = [] # (idx, height)
        max_a = 0

        for idx, height in enumerate(heights):
            recent_pop = None
            # while the top of the stack is less than the curr elem it can't be extended further, pop it, and calculate the max area it can form
            while active_heights and height < active_heights[-1][1]: 
                recent_pop = active_heights.pop()
                recent_a = (idx - recent_pop[0]) * recent_pop[1] # b * h, where b is the diff between the current idx and the recent pop's left bound
                max_a = recent_a if recent_a > max_a else max_a
            
            if recent_pop:
                active_heights.append((recent_pop[0], height)) # since the value we're adding was less than the most recently popped element, it can be extended just as far. elem to the left is null or greater.
            else:
                active_heights.append((idx, height)) # if nothing was popped, we have a 1xh rectangle that can't be extended to the left
            
        # for leftover elements: simply calculate b * h, as any remaining element can be extended to the end of the array   
        while active_heights:
            recent_pop = active_heights.pop()
            curr_a = recent_pop[1] * (len(heights) - recent_pop[0])
            max_a = curr_a if curr_a > max_a else max_a
        

        return max_a

        





            