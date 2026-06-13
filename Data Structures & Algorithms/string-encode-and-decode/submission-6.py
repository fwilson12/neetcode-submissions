class Solution:

    def encode(self, strs: List[str]) -> str:
        
        return "|".join(strs)

    def decode(self, s: str) -> List[str]:
        
        res = []
        chars = ""
        for letter in s:
            if letter == '|':
                res.append(chars)
                chars = ""
            else:
                chars += letter
        res.append(chars)
        return res