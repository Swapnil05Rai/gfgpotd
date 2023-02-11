def getMinimumDays(N: int, s: str, P: List[int]) -> int:
    p = {v: i for i, v in enumerate(P)}
    
    day = 0
    for i in range(N-1):
        if s[i] != s[i+1] or p[i] <= day or p[i+1] <= day:
            continue
        day = min(p[i], p[i+1])
        
    return day if day == 0 else day+1

  
  
"""This code is finding the minimum number of days required to satisfy the condition that if s[i] != '?' then s[i] != s[i+1] in a string s of length N.
The permutation of the string indices is given in the list P.

First, the permutation is stored in a dictionary p where the keys are the indices and the values are the values of P at those indices.

Next, a variable day is used to keep track of the minimum number of days required.
The for loop iterates over s from index 0 to N-1, checking if s[i] is equal to s[i+1] and if the indices i and i+1 in P are less than or equal to day.
If either of these conditions are not met, then the loop continues to the next iteration.

If both conditions are met, then the value of day is updated to be the minimum of p[i] and p[i+1].

Finally, the result is returned as day+1 if day is not 0, otherwise it is returned as day"""
