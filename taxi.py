class Solution:
    def minimumTime(self, N : int, cur : int, pos : List[int], time : List[int]) -> int:
        # code here
        mn = float('inf')
        for i in range(N):
            mn = min(abs(cur-pos[i])*time[i],mn)
        return mn
      
"""N: an integer representing the total number of positions
cur: an integer representing the current position
pos: a list of integers representing the positions of all the items
time: a list of integers representing the time taken to pick up each item
The function iterates through each position in the "pos" list and calculates the time taken to reach that position from the current position. The time taken is calculated as the absolute difference between the current position and the position of the item multiplied by the time taken to pick up that item.

The minimum time taken to pick up any item is then stored in the "mn" variable using the "min" function. Finally, the function returns the minimum time taken to pick up any item.

In short, the function calculates the minimum time required to pick up an item from a list of positions and their respective pickup times, given the current position."""
