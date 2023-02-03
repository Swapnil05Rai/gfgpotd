class Solution:
    def endPoints(self, matrix, m, n):
        
        n = len(matrix)
        m = len(matrix[0])
        d = 'r'
        i = 0
        j = 0
        
        while (i < n and j < m):
            if matrix[i][j] == 0:
                if d == 'r':
                    if j + 1 == m:
                        return (i, j)
                    else:
                        j += 1
                elif d == 'd':
                    if i + 1 == n:
                        return (i, j)
                    else:
                        i += 1
                elif d == 'l':
                    if j - 1 < 0:
                        return (i, j)
                    else:
                        j -= 1
                else:
                    if i - 1 < 0:
                        return (i, j)
                    else:
                        i -= 1
            else:
                if d == 'u':
                    d = 'r'
                    matrix[i][j] = 0
                elif d == 'r':
                    d = 'd'
                    matrix[i][j] = 0
                elif d == 'd':
                    d = 'l'
                    matrix[i][j] = 0
                else:
                    d = 'u'
                    matrix[i][j] = 0
        
        return ()
    
    
"""This is a implementation of the algorithm to find the last cell before the pointer gets outside of the matrix,
given a binary matrix and the operations that can be performed on it.

The function takes a 2-dimensional vector "matrix" as input and returns the indices of the matrix which leads to outside the matrix from the traversal of the matrix
from the cell (0, 0).

Initially, the direction of movement is set to "right" and the position of the pointer is set to (0, 0). 
Then, the algorithm enters a while loop, and runs until either i becomes greater than or equal to n or j becomes greater than or equal to m.
In each iteration of the loop, the value at matrix[i][j] is checked.

If the value is 0, the direction of movement is checked and the next cell is updated accordingly. 
If the pointer reaches the end of the row (j + 1 == m) or end of the column (i + 1 == n) or the beginning of the row (j - 1 < 0) or the beginning of the column (i - 1 < 0), 
the function returns the current cell (i, j).

If the value is 1, the direction of movement is updated and the value at matrix[i][j] is set to 0. 
The direction of movement is updated in the order "up", "right", "down", "left".

Finally, if the loop finishes execution, the function returns an empty pair."""
