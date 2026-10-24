class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        ans.sort()
        for i, a in enumerate(intervals):
            if not len(ans):
                ans.append(a)
            if ans[-1][1] >= a[0]:
                ans[-1] = [ans[-1][0], max(ans[-1][1], a[1])]
            else:
                ans.append(a)
        return ans
            