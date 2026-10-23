class Solution:
    def reverseBits(self, n: int) -> int:
    
        res = 0
        for i in range(32):
            res += (1 & n >> (32 - i - 1)) * 2**i

        return res


