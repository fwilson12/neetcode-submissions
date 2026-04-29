class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = "1234567890abcdefghijklmnopqrstuvwxyz"
        p1 = 0
        p2 = len(s) - 1
        while p1 < p2:
            if s[p1].lower() not in chars:
                p1 += 1
                continue
            if s[p2].lower() not in chars:
                p2 -= 1
                continue
            if s[p1].lower() != s[p2].lower():
                return False
            p1 += 1
            p2 -= 1
        return True
            
                
             