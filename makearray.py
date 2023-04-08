from typing import List

class Solution:
    def makeBeautiful(self, arr: List[int]) -> List[int]:
        n = len(arr)
        stack = []
        for i in range(n):
            if stack:
                if (stack[-1]>=0 and arr[i]<0) or (stack[-1]<0 and arr[i]>=0):
                    stack.pop()
                else: stack.append(arr[i])
            else: stack.append(arr[i])
        return stack
      
"""This is the implementation of the makeBeautiful function in Python, which takes in a list of integers arr and returns a list of integers which is a "beautiful" subsequence of arr.

The function starts by initializing an empty stack. It then iterates through each integer in the input list arr. For each integer, it checks if the stack is not empty, and if the last integer in the stack and the current integer have different signs (i.e., one is positive and the other is negative). If this is the case, then it pops the last integer from the stack (because it does not contribute to the "beauty" of the subsequence). Otherwise, it pushes the current integer onto the stack.

After iterating through all integers in arr, the function returns the contents of the stack as the final "beautiful" subsequence of arr."""
