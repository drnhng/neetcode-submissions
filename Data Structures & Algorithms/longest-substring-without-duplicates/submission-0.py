class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        myset = set()
        ans = 0
        curr = 0
        start = 0
        for i, a in enumerate(s):
            if a in myset:
                while a in myset:
                    myset.remove(s[start])
                    start += 1
                    curr -= 1
            
            myset.add(a)
            curr += 1
            ans = max(ans, curr)
        return ans