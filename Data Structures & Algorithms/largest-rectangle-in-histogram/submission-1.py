class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        active_heights = [] # (idx, height)
        max_a = 0

        for idx, height in enumerate(heights):
            recent_pop = None
            while active_heights and height < active_heights[-1][1]:
                recent_pop = active_heights.pop()
                recent_a = (idx - recent_pop[0]) * recent_pop[1]
                max_a = recent_a if recent_a > max_a else max_a
            
            if recent_pop:
                active_heights.append((recent_pop[0], height))
            else:
                active_heights.append((idx, height))
            
        while active_heights:
            recent_pop = active_heights.pop()
            curr_a = recent_pop[1] * (len(heights) - recent_pop[0])
            max_a = curr_a if curr_a > max_a else max_a
        

        return max_a

        





            