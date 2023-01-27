class Solution:
	def CountWays(self, str):
		n = len(str)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1 if str[0] != '0' else 0
        for i in range(2, n + 1):
            if str[i-1] != '0':
                dp[i] += dp[i-1]
            if str[i-2] == '1' or (str[i-2] == '2' and str[i-1] <= '6'):
                dp[i] += dp[i-2]
        return dp[n] % (10**9 + 7)




"""The problem can be solved using dynamic programming. The idea is to create an array dp of size n+1, 
where n is the length of the input string. dp[i] will store the total number of ways to decode the substring str[0...i-1].

We can initialize dp[0] = 1 as an empty digit sequence is considered to have one decoding.

We can then iterate through the string and for each digit,
check if it is valid (not 0) and if it can be combined with the previous digit to form a valid number (less than or equal to 26).
We can then update dp[i] by adding the number of ways to decode the substring str[0...i-2] and the number of ways to decode the substring str[0...i-1].

"""
