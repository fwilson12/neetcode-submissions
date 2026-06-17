from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        charDict = defaultdict(int) # char: int (character: freq in current window)
        L = 0
        charDict[s[L]] += 1 # init chardict with first letter appended
        long = 1
        for R in range(1, len(s)):

            charDict[s[R]] += 1
            # while we can't form a consecutive substring with any of the current chars in the window, try the next window
            while not any(True for ch in charDict.keys() if (R - L + 1) - charDict[ch] <= k):
                # update charDict, move L pointer
                charDict[s[L]] -= 1
                L += 1
             
            # we know we can form a consecutive substring filling the whole window
            long = max(R - L + 1, long)



        return long 