from typing import List

 

class Solution:

    def countZero(self, N: int, K: int, arr: List[List[int]]) -> List[int]:

        res = [0] * K

        rows = [False] * (N+1)

        cols = [False] * (N+1)

        val = N * N

        row, col = 0, 0

        for i in range(K):

            if not rows[arr[i][0]]:

                rows[arr[i][0]] = True

                val = val - N + col

                row += 1

            if not cols[arr[i][1]]:

                cols[arr[i][1]] = True

                col += 1

                val = val - N + row

            res[i] = val

 

        return res


"""The given code is implementing the solution to the problem where a matrix of size N * N is given and K tasks are given,
for each task the position (r, c) is given, 
and the task is to change the value at cell (r, c) to 1 and calculate the number of zeros present in the matrix after each task.

The algorithm is using two arrays rows and cols to store if a row or column has already been changed to 1.
The val variable is used to store the current number of zeros in the matrix. Initially, 
the value of val is set to N * N (the total number of cells in the matrix).

For each task, the code checks if the row has already been changed to 1 using rows[arr[i][0]],
if not, it sets the corresponding element in the rows array to True, decrements val by N, and increments row by 1. 
Similarly, it checks if the column has already been changed to 1 using cols[arr[i][1]], if not, it sets the corresponding element in the cols array to True,
decrements val by N, and increments col by 1.

Finally, the result of each task is stored in the res array, and the res array is returned as the final result."""
