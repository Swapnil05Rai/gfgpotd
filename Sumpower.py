#User function Template for python3
class Solution:
    def numOfWays(self, n, x):
            powers = []
            for i in range(1, n+1):
                v = i**x
                if v > n:
                    break
                powers.append(i**x)
            
            dp = [0]*(n+1)
            dp[0] = 1
            
            for c in powers:
                for j in range(n, c-1, -1):
                    dp[j] += dp[j-c]
            return dp[n]%(10**9+7)
