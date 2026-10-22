class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        candidates.sort()
        self.recurse(candidates, target, [], 0)
        return self.ans

    def recurse(self, candidates: List[int], target: int, curr: List[int], ind: int):
        if target < 0:
            return
        if target == 0:
            self.ans.append(curr[:])
        
        for i in range(ind, len(candidates)):
            if i>ind and candidates[i] == candidates[i-1]:
                continue
            curr.append(candidates[i])
            target -= candidates[i]
            self.recurse(candidates, target, curr[:], i+1)
            target += candidates[i]
            curr.pop()