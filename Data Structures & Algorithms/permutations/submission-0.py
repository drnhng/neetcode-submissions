class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.recurse(nums, nums[:], 0)
        return self.ans
    def recurse(self, nums:List[int], curr: List[int], ind: int):
        if ind == len(nums):
            self.ans.append(curr[:])

        for i in range(ind, len(nums)):
            curr[i], curr[ind] = curr[ind], curr[i]
            self.recurse(nums, curr[:],ind+1)
            curr[i], curr[ind] = curr[ind], curr[i]

                