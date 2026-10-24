class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        start = 0
        end = 0
        currSum = 0
        maxSum = nums[0]
        for i, a in enumerate(nums):
            if currSum < 0:
                currSum = nums[i]
                start = i
                maxSum = max(maxSum, currSum)
                continue
            currSum = currSum + a
            maxSum = max(currSum, maxSum)
        start = len(nums)-1
        currSum = 0
        for i, a in reversed(list(enumerate(nums))):
            if currSum < 0:
                currSum = nums[i]
                start = i
                maxSum = max(maxSum, currSum)
                continue
            currSum = currSum + a
            maxSum = max(currSum, maxSum)
        return maxSum