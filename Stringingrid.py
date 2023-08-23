
class Solution:
    def searchWord(self, grid, word):
            rows = len(grid)
            cols = len(grid[0])
            result = []
        
            # Define directions: (row, col) changes for each direction
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        
            def isValid(row, col):
                return 0 <= row < rows and 0 <= col < cols
        
            def checkDirection(row, col, direction, word):
                for char in word:
                    if not isValid(row, col) or grid[row][col] != char:
                        return False
                    row += direction[0]
                    col += direction[1]
                return True
        
            for row in range(rows):
                for col in range(cols):
                    for direction in directions:
                        if checkDirection(row, col, direction, word):
                            result.append((row, col))
                            break
        
            return result 
