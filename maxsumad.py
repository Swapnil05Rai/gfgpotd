class Solution:
    def findMaxSum(self, arr, n):
        if n == 1:
            return arr[0]
        if n == 2:
            return max(arr[0], arr[1])

        arr[2] += arr[0]
        for i in range(3, n):
            arr[i] += max(arr[i-2], arr[i-3])
        
        return max(arr[n-1], arr[n-2])

      
"""The findMaxSum method takes an integer array arr and an integer n (the size of the array) as input.

The method starts by checking if n is 1 or 2. If n is 1, it returns the first element of the array (arr[0]).
If n is 2, it returns the maximum of the two elements of the array (max(arr[0], arr[1])).

Otherwise, the method updates the third element of the array (arr[2]) by adding the first element of the array (arr[0]).
It then iterates through the rest of the elements (i from 3 to n-1) and
updates each element by adding the maximum of the two elements two or three positions before it (arr[i-2] and arr[i-3]).

Finally, the method returns the maximum of the last two elements of the array (max(arr[n-1], arr[n-2])).

This implementation finds the maximum sum that can be obtained by selecting some consecutive elements of the input array such that
no two selected elements are adjacent."""
