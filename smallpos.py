class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr,n):
        #Your code here
        my=[]
        posi=[]
        my=sorted(set(arr))
        for i in range(len(my)):
            if my[i]>0:
                posi.append(my[i])
        if not posi:
            return 1
        maxi=max(arr)
        for i in range(maxi-1):
            if posi[i]!=i+1:
              return i+1
            
        return maxi+1
