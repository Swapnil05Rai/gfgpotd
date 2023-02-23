class Solution:
    def uniquePaths(self, n: int, m: int, grid: List[List[int]]) -> int:
        mod = int(1e9 + 7)
        dp = [[0 for j in range(m)] for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0 and grid[i][j] != 0:
                    dp[i][j] = 1
                elif grid[i][j] != 0:
                    up = 0 if i == 0 else dp[i-1][j]
                    left = 0 if j == 0 else dp[i][j-1]
                    dp[i][j] = (up + left) % mod
                else:
                    dp[i][j] = 0
        
        return dp[n-1][m-1] % mod

      
"""This is a dynamic programming solution to the Unique Paths problem. The problem asks to find the number of unique paths from the top-left cell of a grid of size n x m to the bottom-right cell of the same grid, where the grid contains some obstacles marked with a value of 0.

The solution uses a 2D dp array of size n x m, where dp[i][j] represents the number of unique paths to reach the cell (i, j). The base case is dp[0][0] = 1, as there is only one way to reach the top-left cell.

For all other cells (i, j), if the grid value at (i, j) is 0, then dp[i][j] is set to 0, as there is no way to reach an obstacle cell. Otherwise, the number of unique paths to reach (i, j) can be found by adding the number of unique paths to reach the cell above it (dp[i-1][j]) and the cell to the left of it (dp[i][j-1]). This is because there are only two ways to reach a cell (i, j), either from the cell above it or from the cell to the left of it.

The final answer is stored in dp[n-1][m-1], which represents the number of unique paths to reach the bottom-right cell."""
