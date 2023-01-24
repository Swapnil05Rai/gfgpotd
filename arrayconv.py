def convert(self,arr, n):
		brr = sorted(arr)
        lst = {}
        for i in range(n):
            lst[brr[i]]=i
        for j in range(n):
            arr[j]=lst[arr[j]]
            
            
"""This code sorts the input array, then creates a dictionary that assigns new indices to each element based on its position in the sorted array.
It then iterates through the original array and assigns each element its new index value from the dictionary, changing the input array to the reduced form.
It has a time complexity of O(nlogn) due to the sorting and O(n) for the second iteration, and takes up O(n) extra space for the dictionary."""
