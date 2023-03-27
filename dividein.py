class Solution:
    def countWaystoDivide(self, N, K):
        a=[]
        for i in range(1,N+1):
            a.append(i)
        n=N
        k=K
        dp=[]
        for i in range(N+1):
            c=[]
            for j in range(N+1):
                d=[]
                for k in range(k+1):
                    d.append(-1)
                c.append(d)
            dp.append(c)
        def coin(i,su,a1):
            if(su==n):
                if(a1==k):
                    return 1
                else:
                    return 0
            if(su>n or i>=n or a1>k):
                return 0
            if(dp[i][su][a1]!=-1):
                return dp[i][su][a1]
            a3=coin(i,su+a[i],a1+1)
            a2=coin(i+1,su,a1)
            dp[i][su][a1]=(a3+a2)
            return dp[i][su][a1]
        return(coin(0,0,0))

      
      
"""The countWaystoDivide function takes two arguments, N and K, and returns the number of ways to divide the integer N into exactly K positive integers.

The function first creates a list a containing the integers from 1 to N, and then initializes a 3D dynamic programming array dp with -1 values.

The main recursive function coin takes three arguments, i for the current index of the list a, su for the current sum, and a1 for the current count of integers used in the partition.

The function checks if the current sum equals N, if so, it checks if the current count of integers used in the partition equals K, if yes, it returns 1, otherwise 0. If the current sum exceeds N or the current index i exceeds the length of the list a, or the current count of integers used in the partition exceeds K, the function returns 0.

If the value for the current state of dp[i][su][a1] is not -1, the function returns it.

Otherwise, the function makes two recursive calls, one by including the current integer a[i] and incrementing the count a1 and sum su and the other by excluding the current integer and incrementing the index i. The function then stores the sum of the two recursive calls in dp[i][su][a1] and returns it.

Finally, the function returns the result of the initial call to coin(0,0,0) as the total number of ways to divide N into K positive integers.


:"""
