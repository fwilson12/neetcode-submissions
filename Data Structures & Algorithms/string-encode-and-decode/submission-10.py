class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return 'This is dumb'
        return "|".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "This is dumb":
            return []
        if not s:
            return [""]
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