class Solution:
    def calc(self, heights: List[int], l: int, r: int):
        length = r-l
        width = min(heights[l], heights[r])
        return length*width

    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        maxArea = -1
        while l < r:
            currArea = self.calc(heights, l, r)
            maxArea = max(maxArea, currArea)
            if heights[l] > heights[r]:
                r -= 1
                continue
            else:
                l += 1
                continue
        return maxArea
        