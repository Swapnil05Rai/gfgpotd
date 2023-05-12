from typing import List
class Solution:
    def arrayOperations(self, n : int, arr : List[int]) -> int:
        ctr=0
        flag=arr[0]==0
        for i in arr:
            if i==0:
                if not flag:
                    ctr+=1
                    flag=True
            else:
                flag=False
        if ctr==0 and not flag:
            return 1
        return ctr if flag else ctr+1
      
"""This code implements the arrayOperations() function that takes an integer n and a list of integers arr of size n as input, and returns an integer representing the minimum number of operations required to make the array arr valid. An array is considered valid if it contains at least one non-zero element and there are no consecutive zeros.

The implementation begins by initializing the ctr and flag variables to 0 and arr[0]==0, respectively. The ctr variable counts the number of times we have to make an operation and the flag variable indicates whether the last element processed was zero or not.

The implementation then iterates through the elements of the array arr. If the current element is zero and flag is False (indicating that the last element processed was not zero), it increments ctr and sets flag to True. If the current element is non-zero, it sets flag to False. Finally, it checks if the ctr variable is 0 and flag is False. If this is true, it returns 1, indicating that there is only one non-zero element in the array. Otherwise, it returns ctr if flag is True (indicating that the last element processed was zero) or ctr+1 if flag is False (indicating that the last element processed was non-zero). This final value represents the minimum number of operations required to make the array valid."""
