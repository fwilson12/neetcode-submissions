class Solution:
    def hammingWeight(self, n: int) -> int:

        res = 0
        for i in range(32):
            if 1 << i & n: res += 1 # bascially masking with ...001, ...010, etc. and checking if n isn't 0 (has a 1 there) 

        return res 
        