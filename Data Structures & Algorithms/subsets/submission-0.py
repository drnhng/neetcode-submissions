class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.recurse(nums, 0, [], ans)
        return ans
    def recurse(self, nums:List[int], ind: int, curr: List[int], ans:List[int]):
        ans.append(curr[:])
        for i in range(ind, len(nums)):
            curr.append(nums[i])
            self.recurse(nums, i+1, curr[:], ans)
            curr.pop()
