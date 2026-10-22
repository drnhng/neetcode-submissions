class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dups = set()
        for val in nums:
            if val in dups:
                return True
            dups.add(val)
        return False
