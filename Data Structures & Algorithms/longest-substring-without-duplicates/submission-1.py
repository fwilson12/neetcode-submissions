class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       
        # edge
        if not s:
            return 0

        # init pointers, window character set (init'd with first elem), and max (res)
        L, R = 0, 1
        charset = set({s[0]})
        maxLen = 1

        # letting R slide, starting at 1 since we know when R = L length is 1, so start in next case
        for R in range(1, len(s)):
            
            # character at s[R] is not novel; remove element at L until we can safely add s[R]
            while s[R] in charset:
                charset.remove(s[L])
                L += 1
            
            maxLen = max(maxLen, R - L + 1)
            charset.add(s[R]) # we know it's safe to add s[R]

        return maxLen
            


         