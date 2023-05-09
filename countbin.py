 def countStrings(self, N): 
        M = 10**9+7
        
        def matrix_multiply(a, b):
            nonlocal M
            c = [[0, 0], [0, 0]]    # matrix zero
            for i in range(2):
                for j in range(2):
                    for k in range(2):
                        c[i][j] = (c[i][j]+a[i][k]*b[k][j])%M
            return c
        
        def matrix_power(a, n):
            nonlocal M
            ans = [[1, 0], [0, 1]]  # matrix one
            while n > 0:
                if n%2 == 1:
                    ans = matrix_multiply(ans, a)
                a = matrix_multiply(a, a)
                n //= 2
            return ans
                
            
        return matrix_power([[1, 1], [1, 0]], N+1)[0][0]
      
"""This function returns the number of binary strings of length N that do not contain any consecutive 1's. It uses matrix exponentiation to efficiently compute the result.

The function first defines two helper functions: matrix_multiply(a, b) multiplies two 2x2 matrices a and b, and matrix_power(a, n) computes the n-th power of a 2x2 matrix a using matrix exponentiation.

The main function countStrings(N) computes the (N+1)-th Fibonacci number using the identity F(N+1) = [1 1] [F(N+1) F(N)] where the matrix on the right is the N+1-th power of the 2x2 matrix [[1 1], [1 0]]. The function returns the [0,0]-th entry of the resulting matrix, which is F(N+1).

Since the result can be very large, the function takes the result modulo 10^9 + 7 to return the answer.
"""
