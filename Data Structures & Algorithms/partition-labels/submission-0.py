class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        intervals = []
        charset = set()
        for i, c in enumerate(s):
            if c in charset:
                continue
            charset.add(c)
            intervals.append([i, s.rfind(c)])
        merged = []
        print(intervals)
        #merge intervals
        for i, interval in enumerate(intervals):
            if i == 0:
                merged.append(interval)
                continue
            if interval[0] < merged[-1][1]:
                merged[-1] = [merged[-1][0], max(merged[-1][1], interval[1])]
                continue
            else:
                merged.append(interval)
        ans = []
        print(merged)
        for interval in merged:
            ans.append(interval[1]-interval[0]+1)
        return ans