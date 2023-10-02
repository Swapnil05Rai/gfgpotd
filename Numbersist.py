class Solution:
    def distinctSubsequences(self, s):
        # code here
        MOD = 10**9 + 7
        last_occurrence = {}
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        for i, char in enumerate(s, start=1):
            dp[i] = (2 * dp[i - 1]) % MOD
            if char in last_occurrence:
                dp[i] = (dp[i] - dp[last_occurrence[char]] + MOD) % MOD
            last_occurrence[char] = i - 1
        return dp[-1]
