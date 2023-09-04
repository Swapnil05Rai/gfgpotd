from collections import deque

class Solution:
    def fill(self, rows, cols, matrix):
        queue = deque()
        neighbors = [[-1, 0], [0, -1], [0, 1], [1, 0]]
        
        # Identify 'O' cells on the boundary and mark them as visited (-1)
        for row in range(rows):
            for col in range(cols):
                if (row in {0, rows-1} or col in {0, cols-1}) and matrix[row][col] == "O":
                    queue.append([row, col])
                    matrix[row][col] = -1
        
        while queue:
            row, col = queue.popleft()
            for dx, dy in neighbors:
                new_row, new_col = row + dx, col + dy
                
                # Check if the neighbor is within bounds and is an unvisited 'O'
                if -1 < new_row < rows and -1 < new_col < cols and matrix[new_row][new_col] == 'O':
                    queue.append([new_row, new_col])
                    matrix[new_row][new_col] = -1
        
        # Restore the visited (-1) cells to 'O' and change remaining 'O' cells to 'X'
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == -1:
                    matrix[row][col] = 'O'
                elif matrix[row][col] == 'O':
                    matrix[row][col] = 'X'
        
        return matrix
