class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = [c.lower() for c in s if c.isalnum()]
        if not len(s):
            return True

        start = 0
        end = len(s)-1
        while(start < end):
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True