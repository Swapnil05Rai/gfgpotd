from typing import List
class Solution:
    def goodStones(self, n: int, arr: List[int]) -> int:
        visited = [0] * n
        
        def dfs(i):
            nonlocal arr, visited, n
            
            if i < 0 or i >= n:
                return True
                
            if visited[i] > 0:
                return visited[i] == 2

            visited[i] = 1
            if dfs(i+arr[i]):
                visited[i] = 2
                return True
                
            return False
            
        return sum(dfs(i) for i in range(n))

   
  
"""This is the same code as the previous Python implementation of the goodStones function, with a minor modification.

The only difference is that the function signature has been updated to use type hints, which is a way of specifying the expected type of arguments and return values for functions in Python.

from typing import List imports the List type hint from the typing module.

def goodStones(self, n: int, arr: List[int]) -> int: specifies that the goodStones method takes two arguments: an integer n, and a list of integers arr. The method returns an integer.

In the rest of the function, the visited list is initialized to all zeroes, and the dfs function is defined to perform a depth-first search on the stone positions. The sum function is used to count the number of stones that can be reached from the starting positions"""
