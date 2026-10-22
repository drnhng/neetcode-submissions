class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        nums.sort()
        print(nums)
        self.recurse(nums, [], 0)
        return self.ans
    def recurse(self, nums:List[int], curr:List[int], ind: int):
        self.ans.append(curr[:])
        if ind >= len(nums): 
            return
        for i in range(ind, len(nums)):
            if i > 0 and i>ind and nums[i-1] == nums[i]:
                continue
            curr.append(nums[i])
            self.recurse(nums, curr[:], i+1)
            curr.pop()

