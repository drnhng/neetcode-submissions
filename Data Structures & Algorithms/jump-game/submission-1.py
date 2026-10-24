class Solution:
    def canJump(self, nums: List[int]) -> bool:
        return self.recurse(nums, 0)
    def recurse(self, nums:List[int], ind: int):
        if ind >= len(nums)-1:
            return True
        if nums[ind] == 0:
            return False
        ans = False
        for i in range(nums[ind]+1):
            if i == 0:
                continue
            print(ind + i)
            ans = ans or self.recurse(nums, ind + i)
        return ans