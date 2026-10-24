class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mymap = {}
        ans = 1
        for ind, val in enumerate(nums):
            if val in mymap:
                continue
            count = 1
            if (val-1) in mymap:
                count += mymap[val-1]
            if (val+1) in mymap:
                count += mymap[val+1]
            mymap[val] = count
            checkBot = val-1
            while(checkBot in mymap):
                mymap[checkBot] = count
                checkBot -= 1
            checkTop = val+1
            while(checkTop in mymap):
                mymap[checkTop] = count
                checkTop += 1
            
            ans = max(ans, count)
        return ans