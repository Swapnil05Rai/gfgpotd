class Solution:
    def cutRod(self, price, n):
        #code here
        
        arr = [0]*(n+1)
        arr[1] = price[0]
        for i in range(2,n+1):
            m = 0
            for j in range(1,i):
                m = max(m, arr[j]+arr[i-j])
            m = max(m,price[i-1])
            arr[i] = m
        
        return arr[-1]
