class Solution:
    #Function to sort a list using quick sort algorithm.
    def quickSort(self,arr,low,high):
        # code here
        if len(arr)<2:
            return arr
        else:
            pivot=arr.pop()
            smaller=[i for i in arr if i<=pivot]
            greater=[i for i in arr if i>pivot]
            arr[:] =self.quickSort(smaller,0,len(smaller))+[pivot]+self.quickSort(greater,0,len(greater))
        return arr
    def partition(self,arr,low,high):
        pass
