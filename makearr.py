def minOperations(self, N):
        # Code here
        n=N//2
        res=(n)*(n+1)
        if (N%2!=0):
            return res
        else:
            return res-n
          
          
"""This function calculates the minimum number of operations needed to make all the elements of an array equal. The input parameter N represents the number of elements in the array.

The function first divides N by 2 and stores the result in variable n. It then calculates the sum of the first n even numbers, which is n*(n+1). If N is odd, this sum is returned as the result. If N is even, the sum is subtracted by n and returned as the result. The reason for subtracting n is that if N is even, then we only need to perform half of the operations on the array to make all elements equal, since we can pair up the elements and perform the same operation on each pair."""
