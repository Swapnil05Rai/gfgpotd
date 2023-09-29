from typing import List
from collections import deque

class Solution:    
    def numberOfEnclaves(self, grid: List[List[int]]) -> int:
        # Define the possible neighbor directions
        neighbors = [[0, -1], [-1, 0], [1, 0], [0, 1]]
        
        # Get the dimensions of the grid
        rows, cols = len(grid), len(grid[0])
        
        # Initialize a deque to store boundary points
        boundary = deque()
        
        # Initialize a counter for the number of enclaves
        enclave_count = 0
        
        # Iterate through each cell in the grid
        for i in range(rows):
            for j in range(cols):
                # Check if the cell is land and on the boundary
                if grid[i][j] and (i == 0 or i == rows - 1 or j == 0 or j == cols - 1):
                    boundary.append([i, j])
                # Check if the cell is land and not on the boundary
                if grid[i][j] and 0 < i < rows - 1 and 0 < j < cols - 1:
                    enclave_count += 1
        
        # Process the boundary points using a breadth-first search
        while boundary:
            x, y = boundary.popleft()
            if grid[x][y]:
                # Mark the current cell as visited
                grid[x][y] = 0
                
                # If the cell is not on the inner boundary, decrement the enclave count
                if 0 < x < rows - 1 and 0 < y < cols - 1:
                    enclave_count -= 1
                
                # Check neighboring cells and add valid ones to the boundary
                for dx, dy in neighbors:
                    nx, ny = x + dx, y + dy
                    if -1 < nx < rows and -1 < ny < cols and grid[nx][ny]:
                        boundary.append([nx, ny])
        
        # Return the count of enclaves
        return enclave_count
