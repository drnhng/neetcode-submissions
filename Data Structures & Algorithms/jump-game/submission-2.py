class Solution:
    def canJump(self, nums: List[int]) -> bool:
        visited = [False] * len(nums)
        return self.recurse(nums, 0, visited)
    def recurse(self, nums:List[int], ind: int, visited: List[int]):
        if ind >= len(nums)-1:
            return True
        visited[ind] = True
        
        if nums[ind] == 0:
            return False
        ans = False
        for i in range(nums[ind]+1):
            if i == 0 or visited[ind + i]:
                continue
            print(ind + i)
            ans = ans or self.recurse(nums, ind + i, visited)
        return ans