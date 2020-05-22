class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        profit = 0
        stock = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < stock:
                stock = prices[i]
            elif prices[i] - fee > stock:
                profit += prices[i] - fee - stock
                stock = prices[i] - fee
        return profit
