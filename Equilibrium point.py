class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,A, N):
        # Your code here
        
        if N == 0:
            return -1
        if N == 1:
            return 1
    
        for i in range(1, N):
            A[i] = A[i] + A[i - 1]
        # print(A)
        tsum, lsum, rsum = A[N - 1], 0, 0
        ans = -1
        for i in range(1, N - 1):
            lsum = A[i - 1]
            rsum = tsum - A[i]
    
            if lsum == rsum:
                ans = i + 1
                break
    
        return ans
