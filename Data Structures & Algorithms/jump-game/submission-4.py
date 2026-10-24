class Solution:
    def canJump(self, nums: List[int]) -> bool:
        canReach = [False] * len(nums)
        self.recurse(nums, len(nums)-1, canReach)
        return canReach[0]
    def recurse(self, nums:List[int], ind: int, canReach: List[int]):
        if ind == 0:
            canReach[0] = True
        for i in range(ind-1, -1, -1):
            val = nums[i]
            if val >= ind - i:
                canReach[i] = True
                return self.recurse(nums, i, canReach)
            else:
                continue
            
        return True
        