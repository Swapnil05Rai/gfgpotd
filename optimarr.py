from typing import List


class Solution:
    def optimalArray(self, n : int, a : List[int]) -> List[int]:
        li=[]

        li.append(0)
        
        for i in range(1,n):
        
               li.append(li[0]+li[i-1]+abs(a[i]-a[i//2]))
        
        return li
        
        
        
"""This is a Python class named Solution that defines a single function optimalArray. The function takes two arguments n and a, where n is an integer and a is a list of integers. The function returns a list of integers.

The purpose of the optimalArray function is to compute and return a list li that satisfies the following conditions:

li[0] = 0
For i in the range [1, n-1], li[i] = li[0] + li[i-1] + abs(a[i] - a[i//2]).
The abs function returns the absolute value of a number. The // operator performs integer division (i.e., it returns the quotient of a division rounded down to the nearest integer).

The optimalArray function accomplishes its task by initializing li to [0], and then using a loop to compute each subsequent element of the list according to the formula given above. Finally, the function returns the list li."""
