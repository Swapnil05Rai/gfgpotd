from typing import List


class Solution:
    def totalCuts(self, N : int, K : int, A : List[int]) -> int:
        # code here
        left=[A[0]]
        for i in range(1,N):
            left.append(max(A[i],left[-1]))
        right=[A[-1]]
        for i in range(N-2,-1,-1):
            right.append(min(A[i],right[-1]))
        right=right[::-1]
        ans=0
        for i in range(1,N):
            if left[i-1]+right[i]>=K:
                ans+=1
        return ans
      
"""This function totalCuts takes in three inputs, N, K, and A. N is an integer that represents the length of the array A, K is the maximum value of the sum of any two elements in a non-overlapping subarray of A, and A is a list of integers.

The function calculates two arrays left and right which represent the maximum value of the elements from index 0 to i in A and the minimum value of the elements from index i to N-1 in A, respectively.

Then the function iterates over all indices from 1 to N-1 and checks if the sum of the maximum value in the left subarray up to index i-1 and the minimum value in the right subarray starting from index i is greater than or equal to K. If it is, then it increments the count ans. Finally, the function returns the count of such subarrays.

In other words, the function is trying to find the number of non-overlapping subarrays of A whose maximum value in the left subarray and minimum value in the right subarray sum up to at least K."""
