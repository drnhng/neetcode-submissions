class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for ind, val in enumerate(nums):
            opp = target - val
            if opp in my_dict:
                return [my_dict[opp], ind]
            my_dict[val] = ind 