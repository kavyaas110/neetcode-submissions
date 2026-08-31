class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        dp[i] = min number of coins needed to make amount i
        """
        dp = {}
        min_coins = self.count_min_coins(amount, coins, dp)
        return -1 if min_coins >= 1e9 else min_coins
    
    def count_min_coins(self, amount, coins, dp):
        if amount == 0:
            return 0
        
        if amount in dp:
            return dp[amount]
        else:
            min_coins = 1e9
            for coin in coins:
                if amount-coin >= 0:
                    min_coins = min(min_coins,1+self.count_min_coins(amount-coin, coins, dp))
            
            dp[amount] = min_coins
            return min_coins