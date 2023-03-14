class Solution():
    def maxCoins(self, N, a):
        #your code goes here
        MAX_N = N + 2
        dp = [[0] * MAX_N for _ in range(MAX_N)]
        a.insert(0, 1)
        a.append(1)
        for length in range(0, N - 1 + 1):
            for start in range(1, N - length + 1):
                end = start + length
                max_profit = 0
                for i in range(start, end + 1):
                    profit = (
                        dp[start][i - 1]
                        + a[start - 1] * a[i] * a[end + 1]
                        + dp[i + 1][end]
                    )
                    max_profit = max(max_profit, profit)
                dp[start][end] = max_profit
        return dp[1][N]
  
"""The approach used to solve the problem is dynamic programming. The function initializes a 2D list dp with zeros of size (N+2)x(N+2). It then appends a value of 1 to the beginning and end of the list a to simulate imaginary balloons that are always present.

The function then loops over all possible lengths of subsequences of a, starting from 0 and going up to N-1. For each length, the function loops over all possible starting positions of the subsequence, from 1 to N-length. It then computes the maximum profit that can be obtained by bursting balloons within the subsequence using a nested loop that considers all possible burst positions.

The maximum profit for the current subsequence is stored in the corresponding entry of the 2D list dp. Finally, the function returns the maximum profit that can be obtained by bursting balloons within the entire sequence, which is stored in dp[1][N]."""
