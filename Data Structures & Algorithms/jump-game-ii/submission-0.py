class Solution:
    def jump(self, nums: List[int]) -> int:
        tracker = [1001]*len(nums)
        for i, a in enumerate(nums):
            for ind in range(i+1, min(a+i+1, len(nums))):
                tracker[ind] = min(tracker[a], i)
        print(tracker)      
        count = 1
        i = len(nums)-1
        while i > 0:
            #print(i)
            i = tracker[i]
            count +=1
        return count