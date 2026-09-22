class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit =0
        min_v = prices[0]
        for i in prices[1:]:
            profit = max(i-min_v, profit)
            min_v = min(i, min_v)
        return profit