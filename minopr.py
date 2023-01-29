class Solution:
    def solve(self, a : int, b : int) -> int:
        if a==b:
            return 0
        if (a&b)==a or (a&b)==b:
            return 1
        else:
            return 2
        
"""The given implementation checks if the two input numbers, 'a' and 'b', are already equal, in which case it returns 0 as no operations are needed.
If the bitwise AND of 'a' and 'b' is equal to either 'a' or 'b', the function returns 1 as only one operation is needed to make them equal.
In all other cases, the function returns 2 as two operations are needed to make them equal."""
