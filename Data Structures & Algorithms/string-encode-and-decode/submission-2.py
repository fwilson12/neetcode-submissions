class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        return "|".join(strs)

    def decode(self, s: str) -> List[str]:
        if not s:
            return [s]
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