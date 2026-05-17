class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        max_area = 0
        while i < j:
            area = (j - i) * min(heights[i], heights[j])
            if area > max_area:
                max_area = area 
            
            if heights[j] <= heights[i]:
                j-=1
            else:
                i +=1

        return max_area


        # keep/update max water var
        # water area is just min(ith, jth) * j - i where j is after i. can stop when i = j
        # yeah lets code this out