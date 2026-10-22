class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        count = defaultdict(int)
        if len(s) == 1:
            return 1
        l = 0
        for r in range(len(s)):
            curr = s[r]
            count[curr] += 1
            curr_max = max(count.values())
            if (r-l+1) - curr_max > k:
                while (r-l+1) - curr_max > k:
                    count[s[l]] -= 1
                    l += 1
                    curr_max = max(count.values())
            res = max(res, r-l+1)
        return res