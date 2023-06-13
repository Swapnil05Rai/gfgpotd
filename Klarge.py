class Solution:
     
    def kLargest(self,arr, n, k):
    # code here
        arr.sort()
        new =[]
        for i in range(1,k+1):
            new.append(arr[-i])
        return new
