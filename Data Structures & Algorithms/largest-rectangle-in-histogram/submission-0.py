class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        max_area = 0
        curr_length = 1
        for i in range(len(heights)):
            if i > 0 and heights[i] == heights[i-1]:
                curr_length += 1
            else:
                curr_area = curr_length * heights[i] 
                max_area = curr_area if curr_area > max_area else max_area
                curr_length = 1
        return max_area
            