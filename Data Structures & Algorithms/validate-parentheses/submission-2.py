class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for ch in s:
            if ch == "(" or ch == "[" or ch == "{":
                stack.append(ch)
                continue

            if len(stack) > 0 and self.validPair(stack[-1], ch):
                stack.pop()
            else:
                return False
        
        if len(stack) > 0: # leftovers
            return False
        
        return True


    def validPair(self, opening: str, closing: str) -> bool:
        if (opening == "(" and closing == ")") or (opening == "[" and closing == "]") or (opening == "{" and closing == "}"):
            return True
        else:
            return False

        
        