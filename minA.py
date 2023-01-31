class Solution:
    def minRepeats(self, A, B):
        for i in range(1, len(B)//len(A) + 3): 
            if B in A * i: return i
        return -1
  
  

"""The for loop iterates i from 1 to len(B)//len(A) + 3.
In each iteration, A is repeated i times and stored in the variable A * i.
The in operator is used to check if B is a substring of A * i. If B is found, the function returns i.
If B is not found in any of the repetitions of A, the function returns -1.
Note that the range len(B)//len(A) + 3 is used to ensure that A is repeated enough times to cover the length of B,
and in the worst case, we repeat A one more time to confirm that B is not a substring of A."""
