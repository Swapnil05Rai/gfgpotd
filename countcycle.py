class Solution:
    def countPaths(self, n: int) -> int:
        mod = 10**9 + 7
        ans = 0
        for i in range(1, n):
            ans = ((ans % mod) * 3) % mod
            if i % 2 == 1:
                ans = (ans + 3) % mod
            else:
                ans = (ans - 3) % mod
        return ans % mod

      
"""The code is calculating the number of distinct paths that can be taken to move from the top-left corner of a N x N grid to the bottom-right corner of the grid. The allowed moves are to the right, down, or diagonally down and to the right.

The code iterates over the integers from 1 to N-1 and calculates the number of distinct paths for a grid of size i x i. It uses a formula based on whether i is even or odd to calculate the number of distinct paths for each grid size.

Finally, the code returns the number of distinct paths for the N x N grid, which is the result of the iteration.



"""
