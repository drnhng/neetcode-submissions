class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []
        self.backtrack(nums, [], target, 0)
        return self.res

    def backtrack(self, nums:List[int], curr:List[int], target:int, idx: int):
        if target < 0:
            return 
        if target == 0:
            self.res.append(curr[:])
            return
        for i in range(idx, len(nums)):
            curr.append(nums[i])
            target -= nums[i]
            self.backtrack(nums, curr[:], target, i)
            curr.pop()
            target += nums[i]
