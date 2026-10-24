class Solution:
    def calc(self, midVal: int, piles: List[int]):
        total = 0
        for i, a in enumerate(piles):
            total += a/midVal
        return total

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        mid = (r-l)/2
        minTime = r
        while l < r:
            currTime = self.calc(mid, piles)
            if currTime > h:
                l = mid + 1
                continue
            else:
                minTime = min(minTime, currTime)
                r = mid -1
        return minTime

