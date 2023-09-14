class Solution:
	def perfectSum(self, arr, n, s):
        dp = [1] + [0]*s
        MOD = 10**9 + 7
        for a in arr:
            for i in range(s, a-1, -1):
                dp[i] = (dp[i] + dp[i-a])%MOD
        return dp[s]
