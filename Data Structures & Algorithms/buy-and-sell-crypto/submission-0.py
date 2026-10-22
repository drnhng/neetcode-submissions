class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        ans = -1
        for i, a in enumerate(prices):
            curr_sell = a - prices[buy]
            ans = max(ans, curr_sell)
            if a < prices[buy]:
                buy = i
                continue
        
        return ans