class Solution:

    def calc(self, heights:List[int], start, end):
        l = end - start 
        w = min(heights[end], heights[start])
        return l*w
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights)-1
        maxArea = 0
        while start < end:
            maxArea = max(maxArea, self.calc(heights, start, end))
            if heights[start] > heights[end]:
                end-=1
            else:
                start += 1
        return maxArea