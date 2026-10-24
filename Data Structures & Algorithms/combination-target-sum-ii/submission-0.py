class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        self.recurse(candidates, target, [], 0, set())
        return self.ans

    def recurse(self, candidates: List[int], target: int, curr: List[int], ind: int, tracker: set[tuple[int]]):
        if target < 0:
            return
        if target == 0:
            if tuple(curr) not in tracker:
                tracker.add(tuple(curr))
                self.ans.append(curr[:])
        
        for i in range(ind, len(candidates)):
            curr.append(candidates[i])
            target -= candidates[i]
            self.recurse(candidates, target, curr[:], i+1, tracker)
            target += candidates[i]
            curr.pop()