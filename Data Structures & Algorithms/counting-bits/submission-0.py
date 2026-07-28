class Solution:
    def countBits(self, n: int) -> List[int]:
        
        res = []
        for i in range(n + 1):
            res.append(self.hammingWeight(i))

        return res

    def hammingWeight(self, n: int) -> int:

        res = 0
        for i in range(32):
            if 1 << i & n: res += 1 # bascially masking with ...001, ...010, etc. and checking if n isn't 0 (has a 1 there) 

        return res 