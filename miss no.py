class Solution:
    def MissingNo(self, matrix):
        # Initialize the number of rows and columns in the matrix
        n = len(matrix)

        # Initialize the variables to store the row and column indices of the zero element
        r0, c0 = 0, 0

        # Initialize lists to store the sum of the elements in each row, column, and diagonal
        row = [0] * n
        col = [0] * n
        diag = [0] * 2

        # Initialize variables to store the sum of the row, column, and diagonal containing the zero element
        row0 = 0
        col0 = 0
        diag01 = 0
        diag02 = 0

        # Loop through the rows and columns of the matrix
        for i in range(n):
            for j in range(n):
                # If the current element is a zero, store its row and column indices
                if matrix[i][j] == 0:
                    r0 = i
                    c0 = j
                # Update the sum of the elements in the current row, column, and diagonals
                row[i] += matrix[i][j]
                col[j] += matrix[i][j]
                if i == j:
                    diag[0] += matrix[i][j]
                if j == n - i - 1:
                    diag[1] += matrix[i][j]

        # Store the sum of the row, column, and diagonals containing the zero element
        row0 = row[r0]
        col0 = col[c0]
        diag01 = diag[0] if r0 == c0 else 0
        diag02 = diag[1] if n - r0 - 1 == c0 else 0

        # Set the sum of the row containing the zero element to the sum of an adjacent row
        row[r0] = row[r0 - 1] if r0 > 0 else row[r0 + 1]
        # Set the sum of the column containing the zero element to the sum of an adjacent column
        col[c0] = col[c0 - 1] if c0 > 0 else col[c0 + 1]

        # Create a set to store the sums of the rows, columns, and diagonals
        s = set()
        # Add the sums of the rows, columns, and diagonals to the set
        for x in row:
            s.add(x)
        for x in col:
            s.add(x)
        if r0 != c0:
            s.add(diag[0])
        if n - r0 - 1 != c0:
            s.add(diag[1])

        # If the set has more than one element, it is not possible to find a missing number
        if len(s) > 1:
            return -1
        else:
            # Add the sums of the row, column, and diagonals containing the zero element to the set
            s.add(row0)
            s.add(col0)
            if r0 == c0:
                s.add(diag01)
            if n - r0 - 1 == c0:
                s.add(diag02)
            # If the sethas more than two elements, it is not possible to find a missing number
            if len(s) > 2:
              return -1
            # If the sum of the elements in the row containing the zero element is less than 1, it is not possible to find a missing number
            if row[0] - row0 < 1:
              return -1
            # Return the missing number, which is the difference between the sum of the elements in the row containing the zero element and the sum of the elements in the other rows
            return row[0] - row0
