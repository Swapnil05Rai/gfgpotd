
class Solution:
    def findMaxRow(self, mat, N):
        # Code here
        row = 0
        ans = 0
        for i in range(N):
            count = 0
            for j in mat[i]:
                if j == 1:
                    count += 1
            if ans < count:
                ans = count
                row = i
        return [row,ans]
      
     
"""The given Python code defines a class Solution with a method findMaxRow that takes two arguments: mat which is a 2D matrix of size N x N, and N which is an integer representing the number of rows/columns in the matrix.

The method iterates over each row of the matrix using a for loop and keeps track of the row number with the maximum number of 1's and the maximum number of 1's found so far using two variables row and ans, respectively.

For each row, the method counts the number of 1's in that row by iterating over each element in the row and checking if it is equal to 1. The count of 1's is stored in a variable count.

If the count of 1's in the current row is greater than the maximum count of 1's found so far (ans), then the ans and row variables are updated to the count of 1's and the row number, respectively.

Finally, the method returns a list containing the row number with the maximum count of 1's and the maximum count of 1's found. This list is constructed using square brackets to create a Python list with two elements, row and ans."""
