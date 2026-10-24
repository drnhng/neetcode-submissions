class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        buyInd = 0
        for i, a in enumerate(prices):
            maxProf = max(maxProf, a-prices[buyInd])
            if a < prices[buyInd]:
                buyInd = i
        return maxProf