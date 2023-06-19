class Solution:
    def arrange(self,arr, n): 
        earr=[None]*n
        for i in range(n):
            se=arr[i]
            earr[i]=arr[se]
        arr.clear()
        return arr.extend(earr)
