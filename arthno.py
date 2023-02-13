def inSequence(A, B, C):
    if C > 0 and B < A:
        return 0
    if C < 0 and A < B:
        return 0
    if C == 0:
        return 1 if A == B else 0
    n = B - A
    if n % C == 0:
        return 1
    return 0

  
"""This code implements a solution to check if a given integer B is present in an arithmetic sequence.
The arithmetic sequence is defined by the first term A and the common difference C.

The function checks if C is positive and B is smaller than A. If this is true, B cannot be a term in the sequence, and the function returns 0. 
If C is negative and A is smaller than B, B also cannot be a term in the sequence, and the function returns 0.

Next, the function checks if C is equal to 0. If this is true, it means the sequence is a constant sequence,
and the function returns 1 if A is equal to B, and 0 otherwise.

Finally, the function calculates n as the difference between B and A. 
If n is divisible by C (which is determined by checking if the remainder of n divided by C is equal to 0), B is a term in the sequence,
and the function returns 1. If n is not divisible by C, B is not a term in the sequence, and the function returns 0."""
