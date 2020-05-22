class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, min_profit = 0, float('inf')
        for price in prices:
            min_profit = min(min_profit, price)
            max_profit = max(max_profit, price - min_profit)
        return max_profit
