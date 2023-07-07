#User function Template for python3
from heapq import *

class Solution:
    
    #Function to merge the arrays.
    def merge(self,arr1,arr2,n,m):
        # select smallest of them as arr2 
        if n < m:
            self.merge(arr2,arr1,m,n)
        # use arr2 as heap O(1) in since just applying heap property    
        heapify(arr2)
        for i, x in enumerate(arr1):
            # getting minheap top
            y = arr2[0]
            if y < x:
                heapreplace(arr2,x)
                arr1[i] = y
        arr2.sort()
