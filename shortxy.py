class Solution:
    def shortestXYDist(self, G, N, M):
        INV = 10**8
        dp = [[INV] * (M+2) for _ in range(N+2)]
        for r in range(1, N+1):
            for c in range(1, M+1):
                dp[r][c] = 0 if G[r-1][c-1]=='X' else min(dp[r-1][c], dp[r][c-1])+1
        for r in range(N, 0, -1):
            for c in range(M, 0, -1):
                dp[r][c] = min( dp[r][c], 1+dp[r+1][c], 1+dp[r][c+1] )
        ans = min( dp[r][c] for r in range(1, N+1) for c in range(1, M+1) if G[r-1][c-1]=='Y')
        return ans
      
"""The function shortestXYDist takes in a grid G of size N by M, where each cell is either 'X' or 'Y'. It uses dynamic programming to calculate the shortest Manhattan distance from each 'X' cell to the nearest 'Y' cell.

It initializes a 2D array dp of size N+2 by M+2 to a large number INV for all cells, except for cells with 'X', which are set to 0. It then iterates through the array from top to bottom and from left to right, and updates dp[r][c] as the minimum of dp[r-1][c] and dp[r][c-1] plus 1 if the cell is not 'X'.

It then iterates through the array from bottom to top and from right to left, and updates dp[r][c] as the minimum of dp[r][c], 1+dp[r+1][c], and 1+dp[r][c+1].

Finally, it finds the minimum dp[r][c] for all 'Y' cells and returns it as the answer."""
