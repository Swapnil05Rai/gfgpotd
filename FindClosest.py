class Solution:
    def printClosest (self,arr, brr, n, m, x) : 
        #code here
        d=float("inf")
        i=0
        j=m-1
        res=[]
        a=-1
        b=-1
        while i<n and j>=0:
            if abs(arr[i]+brr[j]-x)<d:
                d=abs(arr[i]+brr[j]-x)
                a=arr[i]
                b=brr[j]
                
            if arr[i]+brr[j]>x:
                j-=1
                
            else:
                i+=1
                
        res.extend([a,b])
        return res               
