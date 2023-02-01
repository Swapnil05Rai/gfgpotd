class Solution:
    def distinctColoring(self, N, r, g, b):
        rc, gc, bc = 0, 0, 0
        for i in range(N):
            nrc = r[i] + min(gc, bc)
            ngc = g[i] + min(rc, bc)
            nbc = b[i] + min(rc, gc)
            rc, gc, bc = nrc, ngc, nbc
        return min(rc, gc, bc)

      
"""This code is for a problem of "distinct coloring".
Given a number N and arrays r, g, and b of length N,
the code attempts to find the minimum cost of painting N rooms with three different colors (red, green, and blue) such that no two adjacent rooms have the same color.

The distinctColoring function implements a dynamic programming approach to solve the problem. 
The function has three variables rc, gc, and bc to keep track of the minimum cost of painting the rooms using only red, green, and blue color respectively. 
The function iterates over all the rooms (i in the range [0, N-1]), and updates the values of rc, gc, and bc in each iteration. 
The updated values are the sum of the cost of painting the current room and the minimum cost of painting the previous rooms with the remaining two colors.
Finally, the function returns the minimum of the three values rc, gc, and bc as the answer."""
