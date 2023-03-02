class Solution:
    def minCost(self, costs) -> int:
        import numpy as np
        N, K = len(costs), len(costs[0])
        if N<=0 or K<=0 or (K==1 and N>=2): return -1
        dp, tmp = costs[0].copy(), [0]*K
        for i in range(1, N):
            min1 = np.argmin(dp)
            min2 = min( (v,i) for i, v in enumerate(dp) if i!=min1 )[1]
            for j in range(K):
                tmp[j] = costs[i][j] + (dp[min1] if min1 != j else dp[min2])
            dp, tmp = tmp, dp
        return min(dp)



"""This is a Python function minCost that takes a list of costs and returns the minimum cost to paint all the houses with no adjacent houses having the same color. Here's a brief explanation of the code:

The function takes a 2D list costs where costs[i][j] represents the cost of painting house i with color j. The function returns an integer representing the minimum cost to paint all the houses.

The function first checks if the input is valid: If N<=0 or K<=0 or if K==1 and N>=2, it returns -1.

The function initializes the first row of the DP table dp to be the same as the costs of painting the first house.

Then, for each subsequent house i (starting from the second house), the function computes the minimum cost of painting the current house with each color j given the cost of painting the previous house with the two cheapest colors. It updates the DP table dp accordingly.

Finally, the function returns the minimum value in the last row of the DP table dp."""
