from typing import List
from collections import deque

class Solution:
    def chefAndWells(self, n: int, m: int, c: List[List[str]]) -> List[List[int]]:
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        visited = [[False] * m for i in range(n)]
        dist = [[-1] * m for i in range(n)]
        q = deque()

        for i in range(n):
            for j in range(m):
                if c[i][j] == 'W':
                    q.append([i, j])
                    visited[i][j] = True
                if c[i][j] == 'W' or c[i][j] == '.' or c[i][j] == 'N':
                    dist[i][j] = 0

        dis = 2
        while q:
            size = len(q)
            for p in range(size):
                x = q.popleft()
                i = x[0]
                j = x[1]
                for k in range(4):
                    curri = i + dx[k]
                    currj = j + dy[k]

                    if curri >= 0 and currj >= 0 and curri < n and currj < m and visited[curri][currj] == False and c[curri][currj] != 'N':
                        visited[curri][currj] = True
                        q.append([curri, currj])
                        if c[curri][currj] == 'H':
                            dist[curri][currj] = dis

            dis += 2

        return dist
      
      
"""This is a Python solution to the "Chef and Wells" problem. The problem statement is not provided here, but it involves finding the minimum distance from each cell containing an 'H' (hospital) to the nearest 'W' (well) cell in a 2D grid of size n x m.

The solution uses a breadth-first search (BFS) algorithm to traverse the grid from each 'W' cell and mark all the cells it can reach within an even distance (dis = 2, 4, 6, ...) with a corresponding distance value in the dist matrix. The algorithm stops at the first 'H' cell it encounters in each BFS traversal, and records the distance to that cell in dist.

The solution initializes visited and dist matrices with False and -1 values, respectively. Then it loops over all cells in the grid, and if the cell is a 'W', it appends its indices to a deque and marks it as visited. If the cell is 'W', '.', or 'N', it sets its distance value in dist to 0.

The BFS algorithm starts by dequeuing the next cell in the queue, and looping over its neighbors. If a neighbor cell is within the bounds of the grid, hasn't been visited yet, and is not an 'N' cell, it is marked as visited and its indices are enqueued. If the neighbor cell is an 'H', its distance value in dist is set to the current value of dis.

The BFS algorithm stops after all reachable cells from 'W' cells have been visited and marked in dist. Finally, the function returns the dist matrix."""
