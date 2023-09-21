class Solution:  
    
    #Function to find the maximum money the thief can get.
    def FindMaxSum(self,a, n):
        
        if n == 0:
            return 0
        if n == 1:
            return a[0]
        
        dp = [0] * n
        
        # Base cases
        dp[0] = a[0]
        dp[1] = max(a[0], a[1])
        
        for i in range(2, n):
           
            dp[i] = max(dp[i-1], dp[i-2] + a[i])
        
        return dp[n-1]
