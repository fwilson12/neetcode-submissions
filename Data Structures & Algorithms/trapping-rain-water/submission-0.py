class Solution:
    def trap(self, height: List[int]) -> int:
        
        size = len(height)

        lmax = [height[0]]
        rmax = [height[-1]]


        for i in range(1, size):
            lmax.append(max(height[i], lmax[i-1]))

        for i in range(size - 2, -1, -1):
            rmax.append(max(height[i], rmax[-1]))
        rmax.reverse()

        res = 0
        for i in range(size):
            res += min(rmax[i], lmax[i]) - height[i]
        return res

    
            

