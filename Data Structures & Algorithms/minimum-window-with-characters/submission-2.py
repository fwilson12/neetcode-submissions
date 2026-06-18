class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        tHash = {} # char: int (count)
        # init tHash for comparison later
        for char in t:
            if char not in tHash:
                tHash[char] = 1
            else:
                tHash[char] += 1
        
        currChars = {}
        L = 0
        shortStrLen = float("infinity")
        shortStr = ""
        for R in range(len(s)):

            # only add the char to currChars if it's relevant (in tHash)
            if s[R] in tHash:
                if not s[R] in currChars:
                    currChars[s[R]] = 1
                else:
                    currChars[s[R]] += 1
            
            # while curr window includes all chars in t, see how small we can get it (NOTE: the current window substring can have more than enough of t's chars to count, so a simple hashmap comparison is not sufficient)
            while all((char in currChars and char in tHash) and currChars[char] >= tHash[char] for char in tHash):
                subStrLen = R - L + 1
                if subStrLen < shortStrLen:
                    shortStr = s[L:R+1]
                    shortStrLen = subStrLen
                if s[L] in tHash: # only if relevant
                    currChars[s[L]] -= 1 # don't need to delete, as we need the value of s[L] to eventually equal s[L]'s value in tHash for a comparison to be true
                L += 1 # see if we can go smaller




        return shortStr