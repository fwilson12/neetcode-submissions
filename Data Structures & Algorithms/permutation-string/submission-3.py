from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # edge case
        if len(s1) > len(s2):
            return False

        # initialize s1Dict for comparison
        s1Dict = defaultdict(int)
        for ch in s1:
            s1Dict[ch] += 1

        # initialize pointers & window char dict
        L = 0
        charDict = defaultdict(int)
        # initialize first window + R pointer
        for i in range(len(s1)):
            charDict[s2[i]] += 1
            

        for R in range(len(s1), len(s2)):
            
            # checking if chardict in new window has the same character counts as s1
            if charDict == s1Dict:
                return True
            
            # slide the window, R will increment on its own
            charDict[s2[R]] += 1
            charDict[s2[L]] -= 1
            # for accurate comparison, as s1Dict won't have this empty key
            if charDict[s2[L]] == 0:
                del charDict[s2[L]]
            
            L += 1
        
        # final check after last iteration
        return charDict == s1Dict