class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = prices[0]
        profit = 0
        for price in prices[1:]:
            new_profit = price-min_val
            if new_profit > profit:
                profit = new_profit
            if price<min_val:
                min_val=price
        
        return profit
        