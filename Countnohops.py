class Solution:
    def countWays(self,n):
        # code here
        dp = [0 for _ in range(n+1)]
        dp[0] = 1 
        coins = (1, 2, 3)
        mod = 1000000007
        
        for i in range(n+1) :
            for j in coins :
                new_pos = i+j
                if new_pos <= n : 
                    dp[new_pos] = (dp[new_pos] + dp[i]) % mod
        return dp[n]
