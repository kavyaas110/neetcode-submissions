class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    dp[i][j] = 1
                    continue
                val_left = dp[i][j-1] if j-1 >= 0 else 0
                val_up = dp[i-1][j] if i-1>= 0 else 0
                dp[i][j] = val_left + val_up
        
        return dp[m-1][n-1]

        